// TEMPORARY maintenance mode — delete this file to put hubesol.com back online.
// Returns 503 + Retry-After on the public hosts (tells Google "temporary", keeps the index).
// Per-deployment preview URLs (<hash>.hubesol.pages.dev) still serve the real site for QA.

const BLOCKED_HOSTS = new Set(['hubesol.com', 'www.hubesol.com', 'hubesol.pages.dev']);

const PAGE = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>HubESOL — coming soon</title>
<style>
  :root { --bg:#f7f6f2; --fg:#1d2a24; --accent:#1f5c45; }
  @media (prefers-color-scheme: dark) { :root { --bg:#121815; --fg:#e8ede9; --accent:#6fbf9a; } }
  html,body { margin:0; height:100%; }
  body { display:grid; place-items:center; background:var(--bg); color:var(--fg);
         font:16px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif; padding:0 16px; }
  main { max-width:32rem; text-align:center; }
  h1 { font-size:2rem; margin:0 0 .5rem; color:var(--accent); letter-spacing:-.01em; }
  p { margin:0; opacity:.8; }
</style>
</head>
<body>
<main>
  <h1>HubESOL</h1>
  <p>We're putting the finishing touches on the site. Back very soon.</p>
</main>
</body>
</html>`;

export async function onRequest({ request, next }) {
  const host = new URL(request.url).hostname;
  if (!BLOCKED_HOSTS.has(host)) return next();
  return new Response(PAGE, {
    status: 503,
    headers: {
      'content-type': 'text/html; charset=utf-8',
      'retry-after': '86400',
      'cache-control': 'no-store',
      'x-robots-tag': 'noindex',
    },
  });
}
