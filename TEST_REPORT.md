# GitHub Pages / URL iframe test report

Tested locally on the Mac on 2 November 2026 with Chrome automation (Playwright) and a Python HTTP server.

**815 browser assertions passed; zero captured console errors, JavaScript exceptions or failed HTTP requests in the final run.**

- All five pages at desktop, tablet and phone widths: 1440, 768, 390 and 320 pixels.
- Every main navigation destination clicked from each page at each width.
- Browser back/forward and refresh exercised after navigation.
- Brand/Home link and both previous/next links clicked and checked on every page.
- Mobile menu tested; menu state resets when browser history restores a page.
- All local links/files and displayed images checked, with no horizontal overflow.
- All 20 construction steps retained; individual and open-all/close-all controls exercised.
- Construction-guide download exercised.
- The real linked five-page site loaded inside a local URL iframe and all five menu destinations exercised there.
- Testing used `/alek-birdhouse-website/` as a repository-style path, not only the server root.

Additional checks: JavaScript syntax, Python builder compilation, relative file references, no localhost links in website HTML, manual-only deployment trigger and workflow input files. All eight original image assets match their saved originals byte-for-byte.

The first run found a missing favicon on the local iframe test harness; its reference was fixed. A second run exposed a test timing issue when navigating from Home to Home; the assertion now waits for the document heading. The final full rerun passed.

## Limits

No Git repository or remote is configured in this project. Nothing has been published or had its repository visibility changed. The GitHub Actions workflow was checked locally but has not executed on GitHub. No exact public URL exists, so live response headers, hosted iframe permission and actual Google Sites account behaviour remain unverified. Use GOOGLE_SITES_OPTION_2.md after publishing to verify the hosted result, with the Google Sites button-link fallback if framing is blocked.

The previous pasted HTML embeds are preserved but are not used or deployed by the current workflow. The current iframe checks use the ordinary linked pages by URL.
