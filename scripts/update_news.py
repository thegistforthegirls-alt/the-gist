#!/usr/bin/env python3
"""Generate a sourced edition using public Google News RSS searches. Python stdlib only."""
import datetime as dt, email.utils, html, json, pathlib, re, urllib.parse, urllib.request, xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo
ROOT=pathlib.Path(__file__).resolve().parents[1]
QUERIES={
 'Wellness':'women wellness longevity health fitness',
 'Fashion':'fashion designers runway style trends',
 'Beauty':'beauty skincare makeup cosmetics trends',
 'Finance':'personal finance investing money women',
 'Business':'entrepreneurship startups careers AI business',
 'The Tea':'celebrity entertainment pop culture relationships',
 'Gardening':'gardening plants flowers garden seasonal tips',
}
now=dt.datetime.now(dt.timezone.utc)
cutoff=now-dt.timedelta(hours=48)
stories=[];seen=set()
for category,query in QUERIES.items():
    q=urllib.parse.quote(query+' when:2d')
    url='https://news.google.com/rss/search?q='+q+'&hl=en-US&gl=US&ceid=US:en'
    try:
        req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0 (compatible; TheGist/1.0)'})
        with urllib.request.urlopen(req,timeout=18) as response: root=ET.fromstring(response.read())
        count=0
        for item in root.findall('./channel/item'):
            title=html.unescape(''.join(item.findtext('title','').splitlines())).strip()
            link=item.findtext('link','').strip()
            source=item.find('source'); source=(source.text or '').strip() if source is not None else 'News source'
            raw_date=item.findtext('pubDate','')
            try:published=email.utils.parsedate_to_datetime(raw_date).astimezone(dt.timezone.utc)
            except Exception:continue
            if published<cutoff or published>now+dt.timedelta(minutes=10):continue
            key=re.sub(r'\W+','',title.lower())[:110]
            if not title or not link or key in seen:continue
            seen.add(key)
            raw=item.findtext('description','')
            summary=html.unescape(re.sub('<[^>]*>',' ',raw))
            summary=re.sub(r'\s+',' ',summary).strip()
            if summary.lower().startswith(title.lower()):summary=summary[len(title):].strip(' -—')
            summary=summary[:260].strip()
            stories.append({'category':category,'title':title,'source':source,'url':link,'published':published.isoformat(),'summary':summary})
            count+=1
            if count>=6:break
        print(category,count)
    except Exception as e:print('ERROR',category,str(e))
stories.sort(key=lambda s:s['published'],reverse=True)
output={'updated_at':now.isoformat(),'stories':stories,'note':'Stories sourced from Google News RSS; snippets are excerpts, not independently verified summaries.'}
(ROOT/'data'/'news.json').write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print('Saved',len(stories),'stories')
