#!/usr/bin/env python3
"""Generate static multilingual download pages from the published PDF manifest."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ['ja','en','ko','zh-Hans','zh-Hant','de','fr','es','pt','vi','fil','ne','id','it']
KEYS = {'ja':['ja'],'en':['en'],'ko':['ko'],'zh-Hans':['zh_cn'],'zh-Hant':['zh_tw','zh_hk'],'de':['de'],'fr':['fr'],'es':['es','es_419'],'pt':['pt','pt_pt'],'vi':['vi'],'fil':['fil'],'ne':['ne'],'id':['id'],'it':['it']}
BASE = 'https://tyamada.github.io/manga-prompt-kit'
RAW = 'https://raw.githubusercontent.com/tyamada/manga-prompt-kit/main/releases/pdf-manifest.json'
esc = lambda x: html.escape(str(x), quote=True)

def render():
    manifest = json.loads((ROOT/'releases/pdf-manifest.json').read_text())
    locales = json.loads((ROOT/'scripts/sample-page-locales.json').read_text())
    assert manifest['schema_version'] == 1
    entries = manifest['entries']
    assert entries and len({e['sample_id'] for e in entries}) == len(entries)
    assert len({e['new_download_url'] for e in entries}) == len(entries)
    for e in entries:
        u = urlparse(e['new_download_url'])
        assert u.scheme == 'https' and u.netloc == 'github.com' and not u.query and not u.fragment
        assert re.fullmatch(r'/tyamada/manga-prompt-kit/releases/download/(?!latest/)[A-Za-z0-9._-]+/[A-Za-z0-9._-]+\.pdf', u.path)
        assert u.path.endswith('/'+e['filename'])
        assert re.fullmatch('[a-f0-9]{64}', e['sha256'])
        assert e['bytes'] > 0 and e['pages'] > 0 and e['license'] == 'CC-BY-4.0'
    assert set(e['language_key'] for e in entries) <= {k for ks in KEYS.values() for k in ks}
    stamp = hashlib.sha256((ROOT/'releases/pdf-manifest.json').read_bytes()).hexdigest()
    result = {}
    for lang in LANGUAGES:
        t = locales[lang]
        canonical = BASE+'/samples/'+lang+'/'
        head = '<!doctype html><html lang="'+lang+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+esc(t['title'])+'</title><meta name="description" content="'+esc(t['intro'])+'"><link rel="canonical" href="'+canonical+'"><link rel="stylesheet" href="../samples.css">'
        head += ''.join('<link rel="alternate" hreflang="'+l+'" href="'+BASE+'/samples/'+l+'/">' for l in LANGUAGES)
        body = '<body><header><a class="brand" href="../../">Komairo Hiyori · Manga PDF</a><nav aria-label="'+esc(t['all_languages'])+'">'
        body += ''.join('<a lang="'+l+'" hreflang="'+l+'" href="../'+l+'/"'+(' aria-current="page"' if l == lang else '')+'>'+esc(locales[l]['native_name'])+'</a>' for l in LANGUAGES)
        body += '</nav></header><main><p class="eyebrow">CC BY 4.0 · '+str(len(entries))+' PDF</p><h1>'+esc(t['title'])+'</h1><p class="intro">'+esc(t['intro'])+'</p><p>'+esc(t['note'])+'</p>'
        def section(key):
            subset = sorted((e for e in entries if e['language_key']==key), key=lambda e:e['episode'])
            txt = '<section id="'+key+'" class="locale"><h2>'+esc(locales['region_names'][key])+'</h2>'
            if key=='zh_hk':txt += '<p>'+esc(t['region_note'])+'</p>'
            txt += '<div class="cards">'
            for e in subset:
                txt += '<article><p class="episode">'+esc(t['episode'].format(n=e['episode']))+'</p><h3>'+esc(e['title'])+'</h3><p class="meta">'+esc(e['locale'])+' · '+esc(t['pages'].format(n=e['pages']))+' · '+format(e['bytes']/1000000,'.1f')+' MB</p><a class="download" href="'+esc(e['new_download_url'])+'">'+esc(t['download'])+' · PDF</a><details><summary>'+esc(t['checksum'])+'</summary><code>'+e['sha256']+'</code><p>'+esc(t['size'])+': '+str(e['bytes'])+' bytes</p></details></article>'
            return txt+'</div></section>'
        body += ''.join(section(k) for k in KEYS[lang])
        body += '<details class="others"><summary>'+esc(t['other_languages'])+'</summary>'+''.join(section(k) for ks in KEYS.values() for k in ks if k not in KEYS[lang])+'</details>'
        body += '<section class="about"><h2>'+esc(t['license'])+'</h2><p>'+esc(t['rights'])+'</p><p>'+esc(t['ai'])+'</p><p><a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International</a> · <a href="https://github.com/tyamada/manga-prompt-kit">'+esc(t['source'])+'</a></p><p><a href="'+RAW+'">'+esc(t['json'])+'</a> · <a href="https://github.com/tyamada/manga-prompt-kit/releases/tag/manga-pdf-20261103-v1">GitHub Releases</a></p></section>'
        body += '<section class="about"><h2>'+esc(t['app_links'])+'</h2><ul>'+''.join('<li><a href="https://tyamada.github.io/'+repo+'/">'+name+'</a></li>' for repo,name in [('MihirakiPDFViewer','iOS Viewer'),('MihirakiPDFViewer_Android','Android Viewer'),('MihirakiPDFUtility','iOS Utility'),('MihirakiPDFUtility_Android','Android Utility'),('Folimeld','Folimeld')])+'</ul></section></main><footer>こまいろ日和 / Komairo Hiyori · CC BY 4.0</footer></body></html>\n'
        result[Path('docs/samples')/lang/'index.html'] = head+'</head>'+body
    landing = '<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Manga PDF downloads · 14 languages</title><link rel="stylesheet" href="samples.css"><main><p class="eyebrow">Komairo Hiyori · CC BY 4.0</p><h1>Manga PDF downloads</h1><p>サンプルPDFマンガ · Select your language</p><nav>'+''.join('<a lang="'+l+'" href="'+l+'/">'+esc(locales[l]['native_name'])+'</a>' for l in LANGUAGES)+'</nav><p>PDF · 3 episodes · 17 language/region variants</p></main></html>\n'
    result[Path('docs/samples/index.html')] = landing
    result[Path('docs/samples/build-manifest.json')] = json.dumps({'source':'releases/pdf-manifest.json','source_sha256':stamp,'pdf_count':len(entries),'languages':LANGUAGES,'pages':14},ensure_ascii=False,indent=2)+'\n'
    return result

def main():
    args = argparse.ArgumentParser(); args.add_argument('--check',action='store_true'); opts=args.parse_args()
    files=render()
    for rel,content in files.items():
        p=ROOT/rel
        if opts.check:
            assert p.exists() and p.read_text()==content, 'Regenerate '+str(rel)
        else:
            p.parent.mkdir(parents=True,exist_ok=True);p.write_text(content)
    print('Verified' if opts.check else 'Generated', '14 language pages; all published PDF URLs included.')
if __name__=='__main__':main()
