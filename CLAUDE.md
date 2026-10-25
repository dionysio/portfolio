# Portfolio site

Plain static HTML (`index.html` + `public/`), no build step or dependencies.

Deployed as a Cloudflare Worker with static assets (not Pages):
- `wrangler.toml` publishes the repo root (`[assets] directory = "."`). The Worker name must stay `portfolio` to match the dashboard.
- Anything in the repo root that isn't part of the site (docs, config) must be listed in `.assetsignore`, or it gets served publicly.
- Pushes to `master` run `npx wrangler deploy`; PR branches run `npx wrangler preview`, which needs the (empty) `[previews]` block.
