# SPDX-License-Identifier: AGPL-3.0-only
"""Editable SVG article figures. The simplified cover is the current vector master.
Run with --figure cover (default); --figure inline regenerates the older detailed layout.
This script writes SVGs only; publication PNGs are exported separately.
"""
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
    """Current simplified diagram: fixed geometry, native text and vector icons.

    Export the resulting SVG to a 2400 x 1350 PNG for the article cover.
    Edit these coordinates rather than painting over a previously exported PNG.
    """
    navy, blue, teal, red, gold = '#10175E', '#086DD9', '#00A4BD', '#EA233B', '#F4B900'
    pale, mint, cream = '#EAF6FF', '#EDF9FB', '#FFF8E3'
    a = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1680" height="945" viewBox="0 0 1680 945" role="img" aria-labelledby="title desc">',
         '<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->',
         '<title id="title">Evidence-Gated Agents — evidence before AI proceeds</title>',
         '<desc id="desc">Working AI plans within existing permission and proposes a step to an EGA check. Evidence sources feed an evidence service available to every check. Proceed permits the checked step, followed by an outcome record, with optional further work returning to Working AI. Do not proceed leads to remaining stopped and recording the reason. Permitted revision returns to Working AI for rechecking. Human judgement is conditional. People receiving or affected by results and human accountability remain visible. Crossing lines do not join.</desc>',
         '<rect width="1680" height="945" fill="white"/>',
         '<g font-family="Arial, Helvetica, sans-serif">']

    def label(x, y, value, size=24, color=navy, bold=False, anchor='start'):
        a.append(text(x,y,value,size,color,700 if bold else 400,anchor))

    def box(x,y,w,h,fill=pale,stroke=blue,r=14,sw=2):
        a.append(rect(x,y,w,h,fill,stroke,r,sw))

    def line(d,color=teal,sw=5,dash=None):
        a.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linejoin="round"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>')

    def arrow(x1,y1,x2,y2,color=teal,sw=16,head=30):
        # Explicit heads keep incoming and outgoing arrow thickness identical.
        if y1 == y2:
            sign=1 if x2>x1 else -1
            end=x2-sign*head
            line(f'M{x1} {y1} H{end}',color,sw)
            pts=f'{end},{y2-head*.7} {x2},{y2} {end},{y2+head*.7}'
        else:
            sign=1 if y2>y1 else -1
            end=y2-sign*head
            line(f'M{x1} {y1} V{end}',color,sw)
            pts=f'{x2-head*.7},{end} {x2},{y2} {x2+head*.7},{end}'
        a.append(f'<polygon points="{pts}" fill="{color}"/>')

    def icon(kind,x,y,scale=1,color=blue):
        shapes={
            'doc':'<path d="M8 3 H39 L54 18 V65 H8 Z M39 3 V18 H54 M20 31 H42 M20 42 H42 M20 53 H36"/>',
            'locked_doc':'<path d="M8 3 H39 L54 18 V65 H8 Z M39 3 V18 H54"/><rect x="20" y="35" width="24" height="21" rx="2" fill="currentColor" stroke="none"/><path d="M25 35 V30 A7 7 0 0 1 39 30 V35"/><path d="M32 42 V48" stroke="white" stroke-width="3"/>',
            'lock':'<rect x="10" y="29" width="44" height="35" rx="4" fill="currentColor" stroke="none"/><path d="M20 29 V18 A12 12 0 0 1 44 18 V29"/><path d="M32 44 V51" stroke="white"/>',
            'search':'<circle cx="27" cy="27" r="21"/><path d="M43 43 L62 62"/>',
            'globe':'<circle cx="34" cy="34" r="30"/><ellipse cx="34" cy="34" rx="15" ry="30"/><path d="M4 34 H64 M10 16 Q34 28 58 16 M10 52 Q34 40 58 52"/>',
            'database':'<path d="M8 15 V53 C8 67 56 67 56 53 V15"/><ellipse cx="32" cy="15" rx="24" ry="11"/><path d="M8 34 C8 49 56 49 56 34 M8 48 C8 63 56 63 56 48"/>',
            'person':'<circle cx="32" cy="16" r="12"/><path d="M10 63 V51 A22 22 0 0 1 54 51 V63 Z"/>',
            'people':'<circle cx="32" cy="14" r="10"/><circle cx="10" cy="24" r="7"/><circle cx="54" cy="24" r="7"/><path d="M16 60 V43 A16 16 0 0 1 48 43 V60 Z M16 39 C4 32 0 43 0 50 V60 H16 M48 39 C60 32 64 43 64 50 V60 H48"/>',
            'shield':'<path d="M32 3 L57 13 V34 Q57 53 32 66 Q7 53 7 34 V13 Z" fill="currentColor" stroke="none"/><path d="M20 33 L29 42 L45 24" stroke="white"/>',
            'brain':'<path d="M32 10 C17 -2 6 9 10 20 C-2 24 1 38 10 42 C0 55 14 68 28 60 M32 10 C47 -2 58 9 54 20 C66 24 63 38 54 42 C64 55 50 68 36 60 M32 8 V63 M10 20 Q24 17 22 31 M10 42 Q24 42 20 54 M54 20 Q40 17 42 31 M54 42 Q40 42 44 54"/>',
        }
        a.append(f'<g transform="translate({x} {y}) scale({scale})" color="{color}" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>')

    # Header and all content share the accepted left margin.
    box(82,28,10,99,gold,'none',5)
    label(110,76,'Evidence-Gated Agents',60,bold=True)
    label(110,126,'Evidence before AI proceeds',40,bold=True)
    label(110,164,'One check, repeated whenever needed',26,blue)

    box(88,188,404,170)
    label(290,227,'Evidence sources',32,bold=True,anchor='middle')
    label(290,260,'Public and permitted private sources',22,blue,anchor='middle')
    for kind,x in [('doc',141),('globe',225),('database',308),('lock',389)]:
        icon(kind,x,280,.92)
    arrow(492,282,575,282)
    box(575,188,415,170)
    label(782.5,227,'Evidence service',32,bold=True,anchor='middle')
    label(782.5,259,'Material, sources and search coverage',21,blue,anchor='middle')
    label(782.5,287,'Available to every check',21,blue,anchor='middle')
    icon('doc',700,299,.72)
    icon('search',791,297,.78)

    # Evidence request and result lanes stay separate.
    line('M735 397 V375',blue,7,'6 4')
    a.append(f'<polygon points="724,376 735,358 746,376" fill="{blue}"/>')
    arrow(840,358,840,400,blue,10,19)
    label(708,385,'Request',18,bold=True,anchor='end')
    label(866,385,'Results',18,bold=True)

    box(88,438,320,216)
    label(248,480,'Working AI',34,bold=True,anchor='middle')
    label(248,515,'Plans and proposes',26,blue,True,'middle')
    label(248,549,'Within existing permission',23,blue,anchor='middle')
    icon('brain',158,567,1.1,teal)
    icon('doc',276,566,1.08)
    # Same centreline, shaft width and arrowhead for entry and proposal.
    arrow(46,541,88,541)
    arrow(408,541,575,541)
    label(492,484,'Proposed',24,teal,True,'middle')
    label(492,515,'next step',24,teal,True,'middle')

    box(575,401,415,276,cream,gold,14,6)
    label(782.5,447,'EGA check',36,bold=True,anchor='middle')
    label(782.5,477,'Before use, release or action',23,blue,anchor='middle')
    for yy,kind,title,detail in [(486,'doc','Evidence','Support, contradiction and gaps'),(541,'people','Authority','Within the mandate?'),(596,'shield','Applicable permissions','Access, processing and disclosure')]:
        box(594,yy,377,51,'#E1F2FF','none',10)
        icon(kind,613,yy+7,.62)
        label(674,yy+23,title,22,blue,True)
        label(674,yy+44,detail,18,blue)
    label(782.5,669,'Requirements depend on the step',18,blue,anchor='middle')

    arrow(990,466,1017,466,teal,14,24)
    arrow(990,618,1017,618,red,14,24)
    box(1017,412,383,106,mint,teal)
    a.append(f'<circle cx="1072" cy="465" r="37" fill="{teal}"/>')
    line('M1055 466 L1068 479 L1091 451','white',9)
    label(1126,453,'Proceed',33,bold=True)
    label(1126,483,'Within checked scope',21,blue)
    label(1126,508,'Carry out the checked step',19,blue)

    # Affected people stay outside the step box, above the outcome record.
    line('M1331 412 V245 H1448',teal,12)
    arrow(1448,245,1475,245,teal,12,26)
    icon('people',1490,190,1.65)
    label(1545,310,'People receiving or',21,blue,anchor='middle')
    label(1545,338,'affected by the result',21,blue,anchor='middle')
    arrow(1400,466,1428,466,teal,14,27)
    box(1428,427,212,78,'white',teal,39,4)
    icon('doc',1446,443,.69,teal)
    label(1498,460,'End · record',19,bold=True)
    label(1498,487,'outcome',21,bold=True)

    box(1017,573,266,94,'#FFF4F5',red)
    a.append(f'<circle cx="1065" cy="620" r="32" fill="{red}"/>')
    line('M1051 606 L1079 634 M1079 606 L1051 634','white',8)
    label(1110,607,'Do not proceed',23,bold=True)
    label(1110,634,'Reason and permitted',17,blue)
    label(1110,656,'next route',17,blue)
    arrow(1283,620,1428,620,red,10,25)
    box(1428,581,212,78,'white',red,39,3)
    icon('doc',1446,596,.69,red)
    label(1498,612,'Remain stopped',16,bold=True)
    label(1498,637,'Record reason',18,blue)

    # An association to refusal, not an extra approval/exit flow.
    line('M1268 667 L1282 679',blue,4,'3 7')
    icon('person',1267,665,.72)
    label(1290,730,'Authorised human',16,blue,True,'middle')
    label(1290,750,'judgement',16,blue,True,'middle')
    label(1290,769,'Where needed',16,blue,anchor='middle')

    # Optional returns enter Working AI from its bottom edge.
    line('M1145 667 V697 Q1145 716 1126 716 H934',blue,5,'12 7')
    line('M616 716 H259 Q240 716 240 697 V675',blue,5,'12 7')
    a.append(f'<polygon points="227,675 240,654 253,675" fill="{blue}"/>')
    label(780,724,'Revise if permitted · recheck',23,blue,anchor='middle')
    # Small underpass at the solid red exit line makes the non-junction explicit.
    line('M1373 518 V610',teal,5,'12 7')
    line('M1373 631 V755 Q1373 776 1352 776 H945',teal,5,'12 7')
    line('M655 776 H188 Q166 776 166 754 V675',teal,5,'12 7')
    a.append(f'<polygon points="153,675 166,654 179,675" fill="{teal}"/>')
    label(800,784,'Further work, if needed',23,teal,anchor='middle')

    box(88,802,1552,90)
    icon('person',461,815,.95)
    icon('locked_doc',544,814,.96)
    line('M632 821 V875',navy,2)
    label(656,846,'Human accountability and oversight',29,bold=True)
    label(656,879,'Restricted records · Challenge · Remedy',24,blue)
    line('M88 921 H681 M1000 921 H1640',blue,2)
    label(841,928,'Data protection throughout',24,blue,anchor='middle')
    a.append('</g></svg>')
    (ROOT/'evidence-gated-agents-before-we-rely-cover.svg').write_text('\n'.join(a),encoding='utf-8')


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

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--figure', choices=['cover', 'inline'], default='cover')
    args = parser.parse_args()
    (cover if args.figure == 'cover' else inline)()
