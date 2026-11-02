#!/usr/bin/env python3
"""Rebuild five static pages and all existing self-contained embed files. Python standard library only."""
from pathlib import Path
import base64,json,mimetypes,re,html
R=Path(__file__).resolve().parent
PAGES=[('home','Home'),('project','My Birdhouse'),('construction','How I Built It'),('birds','Native Birds'),('about','About My Project')]
ALIASES={'designs':('project','designs'),'get-involved':('birds','help'),'resources':('construction','tools'),'updates':('about','')}
TITLE="Alek’s Birdhouse Project – Helping Native Australian Birds"
brand='<svg viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M6 23 24 7l18 16M12 20v22h24V20"/><circle cx="24" cy="24" r="5"/><path d="M24 31v6M5 42h38M8 9l3 5m28-6-3 5"/></svg>'
(R/'assets/favicon.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48"><rect width="48" height="48" rx="10" fill="#193e32"/><path d="M8 23 24 9l16 14M14 20v20h20V20" fill="none" stroke="#d8e8a5" stroke-width="2"/><circle cx="24" cy="25" r="5" fill="#d8e8a5"/></svg>')
def nav(current):
 links=''.join(f'<a href="{slug}.html" data-nav="{slug}"'+(' aria-current="page"' if slug==current else '')+'>'+label+'</a>' for slug,label in PAGES)
 return '<a class="skip" href="#content">Skip to content</a><header class="site-header"><div class="nav-wrap"><a class="brand" href="home.html">Alek’s Birdhouse Project<small>Year 8 Technology Mandatory · 2026</small></a><button class="menu-toggle" aria-expanded="false" aria-controls="main-navigation">Menu</button><nav class="main-nav" id="main-navigation" aria-label="Main navigation">'+links+'</nav></div></header>'

credits='''<details class="credits"><summary>Photography credits &amp; licences</summary><ul><li>Forest: <a href="https://commons.wikimedia.org/wiki/File:Blue_Gum_Walk_eucalypt_forest.jpg" target="_blank" rel="noopener">Blue Gum Walk eucalypt forest</a> · Bembacorolla · <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a>.</li><li>Hero birdhouse: <a href="https://commons.wikimedia.org/wiki/File:Wooden_Birdhouse_on_Birch_Tree.jpg" target="_blank" rel="noopener">Wooden Birdhouse on Birch Tree</a> · Yamola48 · <a href="https://creativecommons.org/publicdomain/zero/1.0/" target="_blank" rel="noopener">CC0</a>.</li><li>Willie Wagtail: <a href="https://commons.wikimedia.org/wiki/File:Willie_wagtail.jpg" target="_blank" rel="noopener">Willie wagtail</a> · Jason Girvan · <a href="https://creativecommons.org/licenses/by-sa/3.0/" target="_blank" rel="noopener">CC BY-SA 3.0</a>.</li><li>Eastern Rosella: <a href="https://commons.wikimedia.org/wiki/File:(1)Eastern_rosella.jpg" target="_blank" rel="noopener">(1)Eastern rosella</a> · Sardaka · <a href="https://creativecommons.org/licenses/by-sa/4.0/" target="_blank" rel="noopener">CC BY-SA 4.0</a>.</li><li>Simple birdhouse: <a href="https://commons.wikimedia.org/wiki/File:Bird_house.jpg" target="_blank" rel="noopener">Bird house</a> · Unbiassed · public domain.</li><li>Photographs resized/compressed and cropped for display. Adapted CC BY-SA photographs retain their respective licences. Stock photographs are reference material, not Alek’s project evidence. Concept illustrations, tool icons and diagrams are original website artwork.</li></ul></details>'''
def footer():
 return '<footer class="site-footer"><div class="wrap"><div class="footer-line"><span>Alek Andriejunas · Year 8 Technology Mandatory · 2026</span><a href="#top">Back to top</a></div>'+credits+'</div></footer>'
dialog=''

photos=json.loads((R/'src/photos.json').read_text())
contents={}
for slug,label in PAGES:
 content=(R/'src/pages'/f'{slug}.html').read_text()
 def apply_photo(m):
  slot=m.group(1)
  if slot not in photos:return m.group(0)
  info=photos[slot];src=info['src'];p=(R/src).resolve()
  if not p.is_relative_to(R) or not p.is_file():raise ValueError(f'Missing/invalid photo for {slot}: {src}')
  alt=html.escape(info['alt'],quote=True);caption=html.escape(info.get('caption','My own project photograph'))
  return f'<figure class="placeholder has-photo" data-photo-slot="{slot}"><img src="{html.escape(src,quote=True)}" alt="{alt}" loading="lazy"><figcaption>{caption}</figcaption></figure>'
 content=re.sub(r'<figure class="placeholder" data-photo-slot="([^"]+)">.*?</figure>',apply_photo,content,flags=re.S)
 contents[slug]=content

def head(title,inline=False):
 css='<style>'+ (R/'assets/styles.css').read_text()+'</style>' if inline else '<link rel="stylesheet" href="assets/styles.css">'
 return '<!doctype html>\n<html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#dce8cf"><meta name="description" content="My Year 8 birdhouse project, with my design, native bird research and 20 building steps."><title>'+title+'</title><link rel="icon" href="assets/favicon.svg" type="image/svg+xml">'+css+'</head>'
for i,(slug,label) in enumerate(PAGES):
 prev=PAGES[i-1] if i else PAGES[-1];nxt=PAGES[(i+1)%len(PAGES)]
 pager=f'<div class="wrap page-next"><a href="{prev[0]}.html">← {prev[1]}</a><a href="{nxt[0]}.html">{nxt[1]} →</a></div>'
 output=head(f'{label} · {TITLE}')+'<body id="top">'+nav(slug)+'<main id="content">'+contents[slug]+'</main>'+pager+footer()+dialog+'<script src="assets/app.js" defer></script></body></html>'
 output=output.replace('href="home.html"','href="index.html"')
 (R/('index.html' if slug=='home' else slug+'.html')).write_text(output)

def uri(path):
 p=(R/path).resolve()
 if not p.is_relative_to(R) or not p.exists():raise ValueError('Embed asset missing: '+str(path))
 mime=mimetypes.guess_type(p.name)[0] or 'application/octet-stream'
 if p.suffix=='.txt':mime='text/plain;charset=utf-8'
 return 'data:'+mime+';base64,'+base64.b64encode(p.read_bytes()).decode()
script=(R/'assets/app.js').read_text()
# All embedded navigation stays inside its frame. Every snippet can start on its own
# requested page and still open related project pages without an external host.
for start,label in [('home','FULL_WEBSITE_EMBED')]+[(s,s+'-embed') for s,_ in PAGES]+[(target,old+'-embed') for old,(target,anchor) in ALIASES.items()]:
 body=nav(start)+'<main id="content">'+''.join(f'<article data-route="{s}"'+(' hidden' if s!=start else '')+'>'+contents[s]+'</article>' for s,_ in PAGES)+'</main>'+footer()+dialog
 for slug,_ in PAGES:body=body.replace(f'href="{slug}.html"',f'href="#{slug}"')
 # Related sections use page/anchor hashes inside the full embed.
 # Keep top and skip links as within-page anchors.
 output=head(TITLE,True)+f'<body class="embed-page" data-start-route="{start}" id="top">'+body+'<script>'+script+'</script></body></html>'
 output=re.sub(r'(src|href)="((?:assets|downloads)/[^"]+)"',lambda m:m.group(1)+'="'+uri(m.group(2))+'"',output)
 output=output.replace("url('forest.jpg')","url('"+uri('assets/forest.jpg')+"')")
 (R/'google-sites'/(label+'.html')).write_text(output)
(R/'.nojekyll').write_text('')
for old,(target,anchor) in ALIASES.items():
 url=target+'.html'+('#'+anchor if anchor else '')
 output='<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0;url='+url+'"><title>Page moved · Alek’s Birdhouse Project</title></head><body><p>This part of my project is now on <a href="'+url+'">'+dict(PAGES)[target]+'</a>.</p></body></html>'
 (R/(old+'.html')).write_text(output)
print('Updated 5 pages, 4 old-URL redirects and all 10 existing Google Sites embed files.')
