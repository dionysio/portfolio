# My portfolio site

Simple portfolio website based on this [HTML template from Ryan Fitzgerald](https://github.com/RyanFitzgerald/devportfolio-template)

### Live demo

[dionysio.com](https://www.dionysio.com)

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

### Deployment

Hosted on Cloudflare Pages. It's plain static HTML, so there is no build step: the repo root is published as-is (see `wrangler.toml`).

- Git integration: framework preset `None`, build command empty, build output directory `/`.
- Manual deploy: `npx wrangler pages deploy`
