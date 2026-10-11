// Turns the inline "Pro tip: ..." that ends a paragraph into its own callout box.
// Works at build time on the rendered HTML tree, so lessons keep writing a plain
// "**Pro tip:** ..." in Markdown and nothing in src/content has to change.
const MARK = /pro tip:/i;

const hasText = (n) =>
  n.type === 'text' ? n.value.trim() !== '' : (n.children || []).some(hasText);

// Split `node` at the first "Pro tip:". Returns { before: [nodes], after: [nodes] } or null.
function split(node) {
  if (node.type === 'text') {
    const m = MARK.exec(node.value);
    if (!m) return null;
    const before = node.value.slice(0, m.index);
    return {
      before: before ? [{ type: 'text', value: before }] : [],
      after: [{ type: 'text', value: node.value.slice(m.index) }],
    };
  }
  const kids = node.children || [];
  for (let i = 0; i < kids.length; i++) {
    const s = split(kids[i]);
    if (!s) continue;
    const beforeKids = [...kids.slice(0, i), ...s.before];
    const afterKids = [...s.after, ...kids.slice(i + 1)];
    const wrap = (children) => ({ ...node, children });
    return {
      before: beforeKids.length ? [wrap(beforeKids)] : [],
      after: [wrap(afterKids)],
    };
  }
  return null;
}

// Replace the leading "Pro tip:" text with a styled label element.
function labelise(nodes) {
  const first = (arr) => {
    for (const n of arr) {
      if (n.type === 'text') {
        const m = /^\s*pro tip:\s*/i.exec(n.value);
        if (!m) return false;
        n.value = n.value.slice(m[0].length);
        n.__label = true;
        return n;
      }
      if (n.children && first(n.children)) return n;
    }
    return false;
  };
  const holder = { children: nodes };
  const walk = (parent) => {
    for (let i = 0; i < parent.children.length; i++) {
      const n = parent.children[i];
      if (n.type === 'text') {
        const m = /^\s*pro tip:\s*/i.exec(n.value);
        if (!m) return false;
        const rest = n.value.slice(m[0].length);
        const label = { type: 'element', tagName: 'span', properties: { className: ['pro-tip-label'] }, children: [{ type: 'text', value: 'Pro tip' }] };
        parent.children.splice(i, 1, label, ...(rest ? [{ type: 'text', value: ' ' + rest }] : []));
        return true;
      }
      if (n.children && walk(n)) return true;
    }
    return false;
  };
  walk(holder);
  return holder.children;
}

// Capitalise the first word after the label, unless it is a taught word ("at = a point").
function capitalise(nodes) {
  let seenLabel = false;
  const walk = (list) => {
    for (const n of list) {
      if (n.type === 'element' && n.properties?.className?.includes('pro-tip-label')) { seenLabel = true; continue; }
      if (n.type === 'text' && seenLabel && n.value.trim()) {
        const lead = n.value.match(/^\s*/)[0];
        const body = n.value.slice(lead.length);
        if (!/^[\w'’-]+ =/.test(body)) n.value = lead + body.charAt(0).toUpperCase() + body.slice(1);
        return true;
      }
      if (n.children && walk(n.children)) return true;
    }
    return false;
  };
  walk(nodes);
}

function visit(node) {
  if (!node.children) return;
  for (let i = 0; i < node.children.length; i++) {
    const child = node.children[i];
    if (child.type === 'element' && child.tagName === 'p') {
      const s = split(child);
      if (s) {
        const out = [];
        if (s.before.some(hasText)) out.push({ ...child, children: s.before });
        const inner = s.after[0].children ? labelise(s.after) : s.after;
        capitalise(inner);
        out.push({
          type: 'element',
          tagName: 'aside',
          properties: { className: ['pro-tip'], ariaLabel: 'Pro tip' },
          children: inner,
        });
        node.children.splice(i, 1, ...out);
        i += out.length - 1;
        continue;
      }
    }
    visit(child);
  }
}

export default function rehypeProTip() {
  return (tree) => visit(tree);
}
