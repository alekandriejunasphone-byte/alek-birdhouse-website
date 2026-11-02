# Option 2 — embed the published website by URL

Your live website URL is:

https://alekandriejunasphone-byte.github.io/alek-birdhouse-website/

## Minimum clicks in Google Sites

1. Open your Google Site in edit mode.
2. Choose **Pages → + → Full page embed**.
3. Give the page a name, paste the live URL above, and choose **Insert**.
4. Check Preview, then publish the Google Site using the school’s required sharing settings.

The website’s own menu opens its five ordinary HTML pages inside the frame. Do not paste code from the old `google-sites/` folder.

If you prefer five native Google Sites pages, use these five URLs as separate full-page embeds:

- Home: https://alekandriejunasphone-byte.github.io/alek-birdhouse-website/
- My Birdhouse: https://alekandriejunasphone-byte.github.io/alek-birdhouse-website/project.html
- How I Built It: https://alekandriejunasphone-byte.github.io/alek-birdhouse-website/construction.html
- Native Birds: https://alekandriejunasphone-byte.github.io/alek-birdhouse-website/birds.html
- About My Project: https://alekandriejunasphone-byte.github.io/alek-birdhouse-website/about.html

## Compatibility and fallback

The published homepage returns HTTP 200 and does not send an X-Frame-Options or Content-Security-Policy header blocking iframe display. All five published pages and their navigation also passed a browser iframe test. The full live suite passed 815 checks; results are recorded in TEST_REPORT.md. Your actual school Google Sites editor and sharing settings still need checking there; a Google Site has not been created or published by this task.

If your account blocks the embed, choose **Insert → Button**, name it **Open my birdhouse website**, and paste the same live URL. This opens the website directly.

## Website updates

The source repository is https://github.com/alekandriejunasphone-byte/alek-birdhouse-website . Commit/push changes, then manually run **Actions → Deploy static birdhouse website → Run workflow**. A URL embed displays the updated hosted files after deployment; no large code paste is needed.

[Official Google Sites instructions](https://support.google.com/sites/answer/90569?hl=en).
