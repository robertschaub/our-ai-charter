# SPDX-License-Identifier: AGPL-3.0-only
"""Editable SVG content/layout sources for two article compositions.
Publication PNGs are separately styled illustrations; this script updates only SVGs."""
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
    a += [text(x+42,y+80,'EGA',72,AMBER,700),text(x+43,y+122,'Analysis + release controls',29,AMBER)]
    if detail:
        for i,(label,question) in enumerate([('Evidence','Analyse support, contradiction & gaps'),('Authority','Within the current mandate?'),('Disclosure','Permitted to release this content?')]):
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
    a=init(w,h,'Evidence-Gated Agents — evidence before reliance','Broader EGA design: Working AI submits a claim, decision or action instruction. The evidence service retrieves material; EGA analyses support, contradiction and gaps. Outside the acting AI, EGA checks evidence, authority and disclosure, then releases or holds that output. Releasing an instruction does not authorise its execution; the resulting action requires its own authority and evidence checks. Records support inspection and challenge. Existing foundations are FactHarbor Alpha and the Our AI Charter Runtime proof of concept. Their integration is the next milestone, not a deployed system.')
    a += [rect(82,72,9,125,'#DA9829',r=4),text(112,132,'Evidence-Gated Agents',76,INK,700),text(114,195,'Evidence before reliance.',43,MUTED)]
    a += [rect(535,240,845,223,'url(#cool)','#B9CDDF',26,2,'filter="url(#shadow)"'),doc_icon(570,266,BLUE,.8),text(633,300,'Evidence service',48,BLUE,700),text(573,367,'Finds evidence on request',43,INK,600),text(573,419,'Includes sources & search coverage',32,MUTED)]
    a += [path('M845 550 V477',BLUE,5,True,True),text(820,499,'Search request',28,BLUE,500,'end'),path('M1090 478 V547',BLUE,5,True),text(1113,505,'Search results',28,BLUE,500)]
    a += [rect(80,602,430,183,'url(#mint)','#ACD7D0',25,2,'filter="url(#shadow)"'),chip(110,635,TEAL,.8),text(184,663,'Working AI',43,TEAL,700),text(111,698,'Output to be checked',22,MUTED),text(111,734,'Claim, decision',27,INK),text(111,768,'or action instruction',27,INK)]
    a += [path('M515 692 H699',TEAL,7,True),text(606,660,'Submits',29,TEAL,500,'middle'),gate(714,554,602,330)]
    a += [text(756,820,'Foundations: FactHarbor Alpha',26,INK,600),text(756,857,'+ Our AI Charter Runtime PoC',26,INK,600)]
    a += [path('M1336 634 H1454',TEAL,7,True),path('M1336 760 H1454',RUST,6,True)]
    a += [rect(1468,579,367,112,'url(#mint)','#9ACCC4',22),text(1498,626,'Released',43,TEAL,700),text(1498,666,'Checked output',29,MUTED),rect(1468,711,367,112,'url(#warm)','#D9AF9D',22),text(1498,757,'Hold',43,RUST,700),text(1498,797,'Resolve the gap',29,MUTED)]
    a += [path('M1015 903 V930',MUTED,4,True),lock(715,942,.7),text(760,973,'Record for inspection & challenge',31,MUTED)]
    save('ega-cover',a,w,h)

def inline():
    w,h=1600,1770
    a=init(w,h,'Evidence-Gated Agents — checks before a claim, decision or action instruction proceeds','Broader EGA design, still to be integrated and evaluated. Authorised external and internal confidential sources feed a retrieval-only evidence service; confidential-source handling requires development. EGA analyses the retrieved material for support, contradiction and gaps, then checks evidence sufficiency, authority and disclosure outside the acting AI. The output — a claim, decision or action instruction — may be released, or held for more evidence, revision and rechecking, or authorised human judgment when needed. A limited decision record supports inspection, challenge and correction. Releasing an instruction does not authorise its execution; the resulting action requires its own authority and evidence checks.')
    a += [rect(70,59,8,119,'#DA9829',r=4),text(99,110,'Evidence-Gated Agents',66,INK,700),text(101,169,'Checks before AI output is released',29,MUTED)]
    a += [path('M73 238 H112',TEAL,4),text(130,249,'Controls outside the acting AI',31,MUTED)]
    # Source access and system-wide confidential handling are separate concerns.
    a += [rect(70,310,535,308,'#FFFFFF','#BDCEDB',22),doc_icon(96,334,BLUE,.7),text(145,370,'Evidence sources',37,INK,700),text(99,418,'External sources',32,MUTED),text(99,460,'Internal confidential sources',32,MUTED),lock(99,487,.75),text(143,520,'Authorized Access',32,BLUE,600)]
    a += [path('M613 450 H688',TEAL,5,True)]
    a += [rect(704,310,826,308,'url(#cool)','#AEC7DE',22,2,'filter="url(#shadow)"'),text(738,374,'Evidence service',46,BLUE,700),text(738,441,'Finds evidence on request',42,INK,600),text(738,497,'Includes sources & search coverage',34,MUTED)]
    a += [path('M845 717 V632',BLUE,5,True,True),text(822,678,'Search request',25,BLUE,500,'end'),path('M1100 632 V717',BLUE,5,True),text(1122,678,'Search results',26,BLUE,500)]
    a += [rect(70,793,385,237,'url(#mint)','#ACD7D0',24,2,'filter="url(#shadow)"'),chip(100,825,TEAL,.7),text(167,864,'Working AI',38,TEAL,700),text(101,913,'Output to be checked',23,MUTED),text(101,950,'Claim, decision',29,INK),text(101,987,'or action instruction',29,INK)]
    a += [path('M464 907 H547',TEAL,6,True),gate(565,735,965,470,True)]
    a += [text(607,1170,'Foundations: FactHarbor Alpha + Our AI Charter Runtime PoC',26,INK,600)]
    a += ['<g transform="translate(0 54)">']
    # Both outcomes follow the same boundary; no compulsory human approval chain.
    a += [path('M775 1170 V1212 H438 V1232',TEAL,5,True),path('M1315 1170 V1232',RUST,5,True)]
    a += [rect(70,1246,535,200,'url(#mint)','#9ACCC4',22),text(99,1293,'Released',39,TEAL,700),text(99,1337,'Claim, decision or',27,INK),text(99,1371,'action instruction',27,INK),text(99,1413,'Release does not authorise execution.',23,MUTED)]
    a += [rect(649,1246,881,200,'url(#warm)','#D9AF9D',22),text(682,1293,'Held — resolve the gap',38,RUST,700),text(682,1349,'Request evidence • Revise and recheck',26,INK),text(682,1401,'Authorised human judgment when needed',27,MUTED)]
    a += [rect(70,1485,710,175,'#FFFFFF','#BDCEDB',22),doc_icon(99,1513,MUTED,.7),text(145,1547,'Decision record',33,INK,700),text(99,1594,'Inspect • Challenge • Correct',29,INK),lock(99,1603,.65),text(137,1633,'Restricted access',26,BLUE)]
    a += [rect(810,1485,720,175,'#F2F6FA','#BDCEDB',22),lock(840,1515,.7),text(885,1547,'System-wide data protection',31,INK,700),text(839,1594,'Protect information during use and storage,',26,INK),text(839,1633,'and whenever it is sent or shared.',26,INK)]
    a += ['</g>']
    save('ega-inline',a,w,h)

cover()
inline()
