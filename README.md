# Alek’s Birdhouse Project

Existing Year 8 Technology Mandatory project, updated locally on the Mac. Five pages: Home (`index.html`), My Birdhouse (`project.html`), How I Built It (`construction.html`), Native Birds (`birds.html`), About My Project (`about.html`). The simple design, photographs, measurements and all 20 steps are preserved.

## Preview locally

From this folder run:

```sh
python3 -m http.server 8765 --bind 127.0.0.1
```

Open http://127.0.0.1:8765/ on your Mac. Stop the server with Control-C. This local preview address is not the URL to put in Google Sites. No installation or backend is needed.

## Publish to GitHub Pages

No Git repository/remote was found in this folder. Nothing was deployed and no visibility was changed. Use an existing repository if you have one, preserving its history and other files, or create one yourself.

1. Add/commit/upload the project contents so `index.html` is at the repository root. Include `.github/workflows/pages.yml` and `.nojekyll`; GitHub Desktop is useful for including hidden files.
2. In GitHub choose **Settings → Pages → Source → GitHub Actions**.
3. When you want to publish, choose **Actions → Deploy static birdhouse website → Run workflow** on the branch with these files.
4. Copy the exact live URL GitHub returns. Uploads and pushes do not automatically run this manual workflow.

The workflow publishes the normal linked HTML pages, assets and construction download. Legacy large embeds and local iframe test pages are excluded. There is no live URL yet.

## Add to Google Sites

Follow `GOOGLE_SITES_OPTION_2.md`: **Pages → + → Full page embed → paste the published GitHub Pages HTTPS URL**. Do not paste HTML from the old `google-sites/` folder. That folder remains for preservation only. A normal Google Sites button linking to the public URL is the fallback if the host blocks framing.

Local URL framing can be tested with `iframe-url-test.html`. Hosted response headers and Google Sites account restrictions cannot be checked until a live URL exists.

## Edit without losing changes

Edit `src/pages/`, `assets/styles.css`, `assets/app.js` or `src/photos.json`, then run `python3 build.py`. This refreshes the five published pages and compatibility files. Root generated HTML is overwritten by the build. Photo replacement instructions and credits are in `IMAGE_REPLACEMENT.md` and `IMAGE_CREDITS.md`.

The four old page URLs redirect to the corresponding current pages. Navigation uses relative native links, so refresh and browser history do not depend on a JavaScript page router. The mobile menu resets when history restores a cached page.

See `TEST_REPORT.md` for the checks actually run. The teacher’s original handout and personal project photographs were not supplied; placeholders and missing-dimension notes remain honest.
