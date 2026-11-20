#!/usr/bin/env python3
"""Check generated sample download pages and all their local links."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
class Links(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.lang=None
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang')
  if 'id' in a:self.ids.add(a['id'])
  if tag in ['a','link'] and 'href' in a:self.links.append(a['href'])
m=json.loads((ROOT/'releases/pdf-manifest.json').read_text());expected={e['new_download_url'] for e in m['entries']};count=0;linkcount=0
for file in sorted((ROOT/'docs/samples').glob('*/index.html')):
 p=Links();p.feed(file.read_text());assert p.lang==file.parent.name
 assert {link for link in p.links if link.endswith('.pdf')}==expected,file
 assert len([link for link in p.links if link.endswith('.pdf')])==len(expected)
 assert p.ids=={e['language_key'] for e in m['entries']}
 for link in p.links:
  parsed=urlparse(link)
  if parsed.scheme or parsed.netloc:assert parsed.scheme=='https';continue
  q=(file.parent/unquote(parsed.path)).resolve()
  if q.is_dir():q=q/'index.html'
  assert q.is_file(),(file,link)
  assert q.is_relative_to(ROOT/'docs'),(file,link)
  linkcount+=1
 count+=1
assert count==14
print(f'PASS: {count} language pages; {len(expected)} PDFs each; {linkcount} local links.')
