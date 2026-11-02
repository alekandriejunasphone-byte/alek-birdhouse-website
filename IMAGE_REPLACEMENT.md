# Replace the personal-photo placeholders

The bundled photographs are reference images. They are never presented as Alek’s build. There are deliberate placeholders for the final build, workshop evidence, original sketches and SketchUp screenshot.

1. Put your image in `assets/`, for example `assets/my-final-birdhouse.jpg`. Use a compressed JPEG/WebP, ideally 1200–1600 pixels wide and under 300 KB. Avoid identifiable classmates unless you have permission to publish their photos.
2. Edit `src/photos.json`. Use the slot names below and give each photo descriptive alternative text. Example:

```json
{
  "final": {
    "src": "assets/my-final-birdhouse.jpg",
    "alt": "My timber birdhouse showing the finished bark roof and front porch",
    "caption": "My finished birdhouse · Alek Andriejunas"
  },
  "workshop": {
    "src": "assets/my-workshop-photo.jpg",
    "alt": "My timber pieces on the workshop bench",
    "caption": "My workshop evidence"
  }
}
```

3. Run `python3 build.py` from the project folder. This validates the file paths, replaces the placeholders everywhere they are used, and embeds your photo data into all Google Sites files.
4. Preview locally, then republish on GitHub or replace the code in Google Sites.

| Slot key | Used for |
| --- | --- |
| `final` | My finished birdhouse: My Birdhouse |
| `workshop` | My workshop photo: How I Built It |
| `sketch` | My original sketch: My Birdhouse |
| `model` | My SketchUp screenshot: My Birdhouse |
| Optional new slots | Add matching `data-photo-slot` placeholders to your source page first |

Leave any unsupplied slot out of the JSON and its honest placeholder remains. The original file is `{}`. Do not use a stock photograph as construction evidence. To use multiple workshop photos, add figures in the relevant `src/pages/*.html` fragment. Preserve useful alt text and captions.

To replace a reference image, update its path in the source fragments/CSS and update the credits in `build.py` and `IMAGE_CREDITS.md`. Then rebuild. The natural and planter illustrations are website concept art, not your own original school sketches; replace the dedicated sketch slots with your real sketches.
