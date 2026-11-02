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


## Published-site verification — 2 November 2026

Repository: https://github.com/alekandriejunasphone-byte/alek-birdhouse-website

Live website: https://alekandriejunasphone-byte.github.io/alek-birdhouse-website/

Successful Pages deployment: https://github.com/alekandriejunasphone-byte/alek-birdhouse-website/actions/runs/41387184452

The original published website commit is 177dd2cfbe4d0bf4e93b1893b81364b4c6e6e7af. Subsequent documentation updates do not change the deployed HTML, CSS, JavaScript or images.

**815 checks passed against the live HTTPS website**, with zero captured console errors, JavaScript exceptions or HTTP errors in the final run. These exercised all five pages at 1440, 768, 390 and 320 pixel widths, all main menu destinations from each page, browser back/forward, refresh, brand and previous/next links, local file links, images and alt text, mobile overflow, all 20 step disclosures, the expand/collapse button and the guide download.

The real hosted pages were then loaded in a browser iframe, with navigation to all five pages verified. Homepage response: HTTP 200. No X-Frame-Options or Content-Security-Policy header blocking framing was present. The first live run exposed an automation timing issue during an iframe reload; the test was adjusted to await full navigation, and the entire live suite was rerun successfully. No website design changes were needed.

The user approved public repository creation and publishing. Nothing was inserted into or published in an actual Google Site; school account settings and the Google Sites editor must still be checked when inserting the URL. The previous local-only limitations above describe the earlier pre-deployment checks; the live verification in this section supersedes them for GitHub hosting and browser iframe support.


## Content-only revision — 2 November 2026

All five pages were shortened in the existing student voice. Main paragraph text dropped from 920 to 458 words (50.2%). Total content dropped from 1828 to 1167 words (36.2%); retained headings, tool lists, measurements, captions and safety points account for the difference. No new class events were added.

An HTML parser confirmed identical tag structures and attributes in all five source fragments. CSS, JavaScript, builder code and all image assets matched the preceding commit byte-for-byte. All 20 construction steps and the measurement table remain. The text download and legacy embeds were refreshed to match. Local browser suite: 267 checks passed, zero failures. Final minor wording edits were checked by the same structure and asset invariants.
