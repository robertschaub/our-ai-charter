# SPDX-License-Identifier: AGPL-3.0-only
"""One editable SVG design system; two publication compositions. No external assets."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[2] / 'docs' / 'Published'
INK = '#173146'
MUTED = '#506775'
TEAL = '#087F82'
BLUE = '#326CA2'
AMBER = '#A96106'
RUST = '#A34E30'

def text(x, y, value, size=32, color=INK, weight=400, anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'

def rect(x,y,w,h,fill='#fff',stroke='none',r=24,sw=2,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def path(d,color=TEAL,sw=6,arrow=False,dash=False):
    marker = {'#087F82':'teal','#326CA2':'blue','#A34E30':'rust','#506775':'slate'}[color]
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"'+(f' marker-end="url(#{marker})"' if arrow else '')+(' stroke-dasharray="12 12"' if dash else '')+'/>'

def doc_icon(x,y,color=TEAL,scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M4 2 H30 L42 14 V54 H4 Z M30 2 V14 H42 M13 26 H32 M13 35 H32 M13 44 H25"/></g>'

def chip(x,y,color=TEAL,scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round"><rect x="10" y="10" width="40" height="40" rx="9"/><rect x="21" y="21" width="18" height="18" rx="4"/>'+''.join(f'<path d="M{n} 1 V10 M{n} 50 V59 M1 {n} H10 M50 {n} H59"/>' for n in [20,30,40])+'</g>'

def lock(x,y,scale=1):
    return f'<g transform="translate({x} {y}) scale({scale})" fill="none" stroke="{BLUE}" stroke-width="3.5" stroke-linejoin="round"><rect x="4" y="19" width="32" height="28" rx="6"/><path d="M11 19 V12 A9 9 0 0 1 29 12 V19 M20 29 V36"/></g>'

def init(w,h,title,desc):
    defs = '<defs><linearGradient id="paper" x2="1" y2="1"><stop stop-color="#F7FAFA"/><stop offset="1" stop-color="#FFFCF6"/></linearGradient><linearGradient id="cool" x2="0.7" y2="1"><stop stop-color="#F7FBFF"/><stop offset="1" stop-color="#E7F0FA"/></linearGradient><linearGradient id="mint" x2="1" y2="1"><stop stop-color="#F0FAF7"/><stop offset="1" stop-color="#DFF1EC"/></linearGradient><linearGradient id="warm" x2="1" y2="1"><stop stop-color="#FFF9F4"/><stop offset="1" stop-color="#F7E8DF"/></linearGradient><linearGradient id="gate" x2="1" y2="1"><stop stop-color="#FFF9E7"/><stop offset="1" stop-color="#F5D88F"/></linearGradient><linearGradient id="edge"><stop stop-color="#F8BD49"/><stop offset="1" stop-color="#D78B1C"/></linearGradient><filter id="shadow" x="-15%" y="-15%" width="130%" height="140%"><feDropShadow dx="0" dy="10" stdDeviation="16" flood-color="#183648" flood-opacity=".08"/></filter>'
    for name,color in [('teal',TEAL),('blue',BLUE),('rust',RUST),('slate',MUTED)]:
        defs += f'<marker id="{name}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L10 5 L0 10 Z" fill="{color}"/></marker>'
    defs += '</defs>'
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc><!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->{defs}<g font-family="Arial, Helvetica, sans-serif">',rect(0,0,w,h,'url(#paper)',r=0)]

def gate(x,y,w,h,detail=False):
    a=[rect(x+10,y+10,w,h,'#E7BE67',r=30),rect(x,y,w,h,'url(#gate)','#D99629',30,3, 'filter="url(#shadow)"'),rect(x,y,14,h,'url(#edge)',r=7)]
    # A restrained boundary emblem, without a tick or implied certification.
    a += [f'<g transform="translate({x+w-112} {y+37})" fill="none" stroke="#BE8120" stroke-width="3" opacity=".55"><path d="M36 0 L67 12 V38 Q66 60 36 77 Q6 60 5 38 V12 Z"/><path d="M8 27 H64 M8 43 H64 M19 59 H53 M36 11 V27 M22 27 V43 M50 27 V43 M36 43 V59"/></g>']
    a += [text(x+42,y+80,'EGA',72,AMBER,700),text(x+43,y+122,'Checks before release',31,AMBER)]
    if detail:
        for i,(label,question) in enumerate([('Evidence','Enough for this recommendation?'),('Authority','Within the current mandate?'),('Disclosure','Permitted to release this content?')]):
            yy=y+153+i*79
            a += [rect(x+32,yy,w-64,64,'#FFFCF2','#E9C884',12),text(x+55,yy+41,label,31,INK,700),text(x+265,yy+41,question,27,MUTED)]
    else:
        for xx,label,ww in [(x+32,'Evidence',165),(x+208,'Authority',170),(x+389,'Disclosure',179)]:
            a += [rect(xx,y+156,ww,55,'#FFFBEE','#E9C884',13),text(xx+ww/2,y+193,label,29,INK,600,'middle')]
    return ''.join(a)

def save(name,a,w,h):
    a.append('</g></svg>')
    stem = 'evidence-gated-agents-before-we-rely' + ('-cover' if name == 'ega-cover' else '')
    (ROOT/f'{stem}.svg').write_text('\n'.join(a),encoding='utf-8')


def cover():
    w,h=1920,1080
    a=init(w,h,'Evidence-Gated Agents — evidence before reliance','Integration milestone: Working AI proposes a recommendation. EGA requests evidence examination from an evidence service, including supporting and contradicting evidence. Outside the acting AI, EGA checks evidence, authority and disclosure, then releases or holds the recommendation. Records support inspection and challenge. Existing foundations are FactHarbor Alpha and the Our AI Charter Runtime proof of concept. Their integration is the next milestone, not a deployed system.')
    a += [rect(82,72,9,125,'#DA9829',r=4),text(112,132,'Evidence-Gated Agents',76,INK,700),text(114,195,'Evidence before reliance.',43,MUTED)]
    a += [rect(535,240,845,223,'url(#cool)','#B9CDDF',26,2,'filter="url(#shadow)"'),doc_icon(570,266,BLUE,.8),text(633,300,'Evidence service',48,BLUE,700),text(573,366,'Supporting',44,INK,600),text(573,414,'evidence',40,INK),text(965,366,'Contradicting',44,INK,600),text(965,414,'evidence',40,INK)]
    a += [path('M845 550 V477',BLUE,5,True,True),text(820,499,'Request',28,BLUE,500,'end'),path('M1090 478 V547',BLUE,5,True),text(1113,505,'Assessment',28,BLUE,500)]
    a += [rect(80,602,430,183,'url(#mint)','#ACD7D0',25,2,'filter="url(#shadow)"'),chip(110,635,TEAL,.8),text(184,663,'Working AI',43,TEAL,700),text(111,735,'Recommendation',34,INK)]
    a += [path('M515 692 H699',TEAL,7,True),text(606,660,'Proposes',29,TEAL,500,'middle'),gate(714,554,602,266)]
    a += [path('M1336 634 H1454',TEAL,7,True),path('M1336 760 H1454',RUST,6,True)]
    a += [rect(1468,579,367,112,'url(#mint)','#9ACCC4',22),text(1498,626,'Release',43,TEAL,700),text(1498,666,'Recommendation',29,MUTED),rect(1468,711,367,112,'url(#warm)','#D9AF9D',22),text(1498,757,'Hold',43,RUST,700),text(1498,797,'Resolve the gap',29,MUTED)]
    a += [path('M1015 839 V866',MUTED,4,True),doc_icon(717,882,MUTED,.6),text(760,909,'Record for inspection & challenge',31,MUTED)]
    a += [path('M85 956 H1835',MUTED,1),text(90,1000,'FOUNDATIONS',23,BLUE,700),text(335,1000,'FactHarbor Alpha  +  Our AI Charter Runtime PoC',34,INK,500),text(335,1046,'Next: connect and evaluate one recommendation workflow.',29,MUTED)]
    save('ega-cover',a,w,h)

def inline():
    w,h=1600,1700
    a=init(w,h,'Evidence-Gated Agents — how a recommendation is checked','Intended recommendation workflow, still to be integrated and evaluated. Permitted external and internal confidential sources feed an evidence service; confidential-source handling requires development. EGA requests examination of supporting and contradicting evidence and checks evidence, authority and disclosure outside the acting AI. A recommendation may be released, or held for missing evidence, a narrower proposal or authorised human judgment when needed. A limited decision record supports inspection, challenge and correction. Release does not execute an action.')
    a += [rect(70,59,8,119,'#DA9829',r=4),text(99,110,'Evidence-Gated Agents',66,INK,700),text(101,169,'What must be checked before a recommendation proceeds?',31,MUTED)]
    a += [path('M73 238 H112',TEAL,4),text(130,249,'Controls outside the acting AI',31,MUTED)]
    # Source path is an intended extension, labelled where it appears rather than in a remote footer.
    a += [rect(70,310,535,308,'#FFFFFF','#BDCEDB',22),lock(96,338,.8),text(145,370,'Evidence sources',37,INK,700),text(99,418,'External sources',32,MUTED),text(99,460,'Internal confidential sources',32,MUTED),text(99,507,'Before use: authorised',30,BLUE,600),text(99,545,'access + processing',30,BLUE,600),text(99,591,'Confidential handling: to build',28,MUTED)]
    a += [path('M613 450 H688',TEAL,5,True),text(650,420,'Permitted',20,TEAL,500,'middle')]
    a += [rect(704,310,826,308,'url(#cool)','#AEC7DE',22,2,'filter="url(#shadow)"'),text(738,374,'Evidence service',46,BLUE,700),text(738,441,'Supporting evidence',42,INK,600),text(738,497,'Contradicting evidence',42,INK,600),text(738,574,'Assesses; does not authorise release.',30,MUTED)]
    a += [path('M845 717 V632',BLUE,5,True,True),text(822,678,'Search / request',25,BLUE,500,'end'),path('M1100 632 V717',BLUE,5,True),text(1122,678,'Assessment',26,BLUE,500)]
    a += [rect(70,793,385,237,'url(#mint)','#ACD7D0',24,2,'filter="url(#shadow)"'),chip(100,825,TEAL,.7),text(167,864,'Working AI',38,TEAL,700),text(101,929,'Proposes an exact',29,INK),text(101,970,'recommendation',29,INK)]
    a += [path('M464 907 H547',TEAL,6,True),gate(565,735,965,416,True)]
    # Both outcomes follow the same boundary; no compulsory human approval chain.
    a += [path('M775 1170 V1212 H438 V1232',TEAL,5,True),path('M1315 1170 V1232',RUST,5,True)]
    a += [rect(70,1246,535,200,'url(#mint)','#9ACCC4',22),text(99,1293,'Released',39,TEAL,700),text(99,1337,'Recommendation + permitted',28,INK),text(99,1371,'evidence summary',28,INK),text(99,1413,'Release does not execute an action.',25,MUTED)]
    a += [rect(649,1246,881,200,'url(#warm)','#D9AF9D',22),text(682,1293,'Held — resolve the gap',38,RUST,700),text(682,1349,'Request evidence • Check a narrower recommendation',26,INK),text(682,1401,'Authorised human judgment when needed',27,MUTED)]
    a += [doc_icon(80,1494,MUTED,.75),text(131,1523,'Decision record',29,INK,700),text(410,1523,'Inspect • Challenge • Correct',28,MUTED),text(1020,1523,'Limited content, access & retention',24,MUTED)]
    a += [path('M80 1572 H1520',MUTED,1),text(80,1625,'EXISTING FOUNDATIONS',23,BLUE,700),text(445,1625,'FactHarbor Alpha + Our AI Charter Runtime PoC',30,INK,500),text(445,1666,'Integration remains to be built and evaluated.',26,MUTED)]
    save('ega-inline',a,w,h)

cover()
inline()
