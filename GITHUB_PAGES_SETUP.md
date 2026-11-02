# GitHub Pages setup

The existing `.github/workflows/pages.yml` is now manual only. It publishes the linked five-page site and assets, excluding old HTML embeds and local test pages. No push-triggered publication is configured.

Follow the GitHub instructions in `GOOGLE_SITES_OPTION_2.md` and `README.md`. Choose **Settings → Pages → GitHub Actions**, then manually **Actions → Deploy static birdhouse website → Run workflow** when ready to publish.

No local Git repository, remote, deployed URL or repository visibility change was created. If you have an existing repository elsewhere, copy/commit these files into that checkout while preserving its unrelated contents. Include the hidden `.github` folder. Use the exact URL GitHub returns after the deployment succeeds.

[Official GitHub Pages workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
