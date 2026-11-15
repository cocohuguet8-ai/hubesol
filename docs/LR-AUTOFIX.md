# LR auto-fix: Learner Review → Claude → publicat

Bucle automàtic per a correccions concretes que troba Learner Review. Aprovat per la Coco el 15/11/2026.

## Com funciona

1. **Learner Review** (actua com a `cocohuguet8-ai`) obre **un issue per problema** amb l'etiqueta `lr-auto` (format a sota).
2. **`.github/workflows/lr-fix.yml`** (només si l'autor i qui posa l'etiqueta és `cocohuguet8-ai`):
   - Claude (claude-code-action, subscripció de la Coco via el secret `CLAUDE_CODE_OAUTH_TOKEN`) llegeix l'issue i edita fitxers. Màx. 25 torns; només pot llegir/editar i executar `npm run validate|lint|build` i `audit_semantic.py`. No fa git.
   - **Guarda**: només fitxers *existents* i *modificats* dins de
     `src/content/lessons/<hub>/<slug>.md`, `src/data/practice/*.json`, `src/data/quizzes/*.json`, `src/components/**` (.astro/.js/.mjs/.ts/.css); màxim **6 fitxers**. Res de `.github/`, `package.json`, lockfiles, config, `scripts/`, `claude/`…
   - **Proves** sobre el canvi exacte: `validate`, `lint`, `build`, `audit_semantic.py .` (0 troballes a totes les lliçons), **lychee** (enllaços interns del `dist/`, offline) i **e2e** (Playwright, ~15 min).
   - Si tot és verd: branca `lr/issue-<n>`, PR «Fixes #n» amb etiqueta `lr-auto`, i estat de commit `lr-gate = success`.
   - Si alguna cosa falla (Claude no canvia res, diu `cannot-fix`, toca fitxers no permesos, falla una prova…): comentari amb el motiu a l'issue i etiqueta `lr-needs-coco`. No es publica res.
3. **`.github/workflows/lr-merge.yml`** (s'activa quan acaba «LR auto-fix», o a mà): fusiona (squash) cada PR `lr-auto` obert si
   - el commit té `lr-gate` verd, els fitxers continuen sent permesos i el PR es pot fusionar net, i
   - avui (dia de Madrid) s'han fet **menys de 10** fusions `lr-auto`.
   Si no: `lr-needs-coco` + comentari (p. ex. «daily cap reached»). Després de fusionar: comentari «Publicat» a l'issue, etiqueta `lr-fixed`, issue tancat, branca esborrada. Cloudflare Pages publica `main` sol.

Per què les proves es fan dins `lr-fix` i no al PR: els PR i pushes fets amb `GITHUB_TOKEN` no disparen altres workflows (`validate.yml` no correria). `workflow_run` sí que es dispara quan acaba `lr-fix`, i per això el gate hi penja.

## Etiquetes

| Etiqueta | Vol dir |
|---|---|
| `lr-auto` | Arreglament automàtic demanat (issue) / PR creat pel bucle |
| `lr-needs-coco` | Aturat: cal una persona |
| `lr-fixed` | Fusionat i publicat |

## Format de l'issue (Learner Review)

- **Títol:** `[LR] <slug>: <problema en una frase>` — p. ex. `[LR] past-perfect: Q3 del gapFill accepta «have went»`
- **Etiqueta:** `lr-auto` (només aquesta)
- **Cos:**

```
## Lliçó
- slug: past-perfect
- hub: verb-tenses
- URL: https://hubesol.com/grammar/verb-tenses/past-perfect/

## On
Fitxer(s) si se saben (p. ex. src/data/practice/past-perfect-practice.json, gapFill Q3) i l'activitat.

## Problema
Què passa ara, citant el text exacte.

## Correcció esperada
Què hauria de dir/fer, tan concret com es pugui.

## Com comprovar-ho
Passos o resposta que ha de passar / fallar.

## Referència
HQ-NNN (valoració a 11_Valoracions)
```

Un problema per issue. Si cal una decisió de la Coco, **no** posar `lr-auto`.

## Desfer un canvi publicat

- **GitHub:** al PR fusionat, botó **Revert** → fusiona el PR de revert (o `git revert <sha>` del commit squash a `main`). Cloudflare torna a publicar sol.
- **Cloudflare Pages (immediat):** Workers & Pages → hubesol → Deployments → desplegament anterior → **Rollback**. Després reverteix també a GitHub perquè el següent push no ho torni a posar.

## Pausar-ho

- Un issue: treure-li `lr-auto` (o posar-li `lr-needs-coco`).
- Tot el bucle: GitHub → Actions → «LR auto-fix» → **Disable workflow** (i/o «LR merge gate» per deixar PRs fets però sense publicar).
- Tornar a provar un issue aturat: treure `lr-needs-coco` i tornar a posar `lr-auto`.
- Publicar un PR aturat pel límit diari: treure `lr-needs-coco` del PR i Actions → «LR merge gate» → Run workflow (número del PR), o fusionar-lo a mà.

## Requisits

- Secret del repo `CLAUDE_CODE_OAUTH_TOKEN` (de `claude setup-token`, dura 1 any).
- Settings → Actions → General → *Workflow permissions*: marcar **Allow GitHub Actions to create and approve pull requests** (si no, el PR no es pot obrir i l'issue queda `lr-needs-coco`).
