# Option 2: add the hosted website by URL

Use the normal five-page website hosted on GitHub Pages. Do not paste the large HTML snippets in `google-sites/`; those are retained legacy files and are not part of this deployment.

## Publish when you are ready

No Git repository or remote is configured in this local project, and nothing has been published. No repository visibility has been changed.

1. Open the GitHub repository you want to use, or create one yourself with the visibility your school requires. Keep the existing repository visibility if using an existing repository.
2. Upload the contents of `alek-birdhouse-website`, not the ZIP itself or an extra containing folder. `index.html`, `assets/` and `.github/` must be at the repository root. If GitHub’s upload interface omits hidden folders, use GitHub Desktop to add/commit/push the extracted folder, or create `.github/workflows/pages.yml` in GitHub with the included workflow text. If using an existing repository, merge these files into its checkout and preserve unrelated files/history.
3. Choose **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. When you choose to publish, select **Actions → Deploy static birdhouse website → Run workflow → select the branch containing these files → Run workflow**. The workflow is manual only; uploading/pushing alone does not trigger it.
5. Wait for the deployment to succeed. Copy the exact **github-pages environment URL** from the deployment or Settings → Pages. That is your website URL.

No exact public URL exists yet. A typical project URL looks like `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`, but do not paste this example literally. Use the actual URL returned by GitHub. A custom domain or user-site repository can produce a different address.

## Put it into Google Sites

1. Open your Google Site in edit mode.
2. Choose **Pages → + → Full page embed**.
3. Name it, for example **My Birdhouse Website**.
4. Paste the exact GitHub Pages HTTPS URL from the successful deployment.
5. Click **Insert** and check Preview. The website menu opens each of its five HTML pages inside the frame.
6. Publish Google Sites with your school’s required settings.

If you want five native Google Sites pages instead, create five full-page embeds using the homepage URL and URLs ending in `project.html`, `construction.html`, `birds.html` and `about.html`.

## Iframe compatibility: what was checked

The local real five-page website was tested in a URL iframe. This project contains no frame-blocking script or framing policy. The large pasted HTML embed is not used in that test.

**Hosted iframe compatibility is not yet verified:** there is no deployed URL to request. Host response headers and the school Google Sites account can affect framing. Once deployed, test the exact public URL in Google Sites Preview and the published Google Site; inspect all five pages, not only Home. A host may block frames with `X-Frame-Options` or a Content-Security-Policy `frame-ancestors` directive. Successful local framing does not prove the eventual host will permit it.

## If embedding is blocked

Use a normal link instead. In the Google Site choose **Insert → Button**, label it **Open my birdhouse website**, paste the exact published HTTPS URL, and click **Insert**. Test the button and publish the Google Site. A normal button link opens the hosted site without requiring it to run inside a frame.

Official references: [Google Sites embed instructions](https://support.google.com/sites/answer/90569?hl=en) and [GitHub Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
