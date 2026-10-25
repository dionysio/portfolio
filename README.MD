# My portfolio site

Simple portfolio website based on this [HTML template from Ryan Fitzgerald](https://github.com/RyanFitzgerald/devportfolio-template)

### Live demo

[dionysio.com](https://www.dionysio.com)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Deployment

Hosted on Cloudflare Workers (static assets). It's plain static HTML, so there is no build step: the repo root is published as-is (see `wrangler.toml`, files listed in `.assetsignore` are skipped).

Deploy: `npx wrangler deploy` (Workers Builds runs this on every push to `master`, and posts a preview URL on PRs).
