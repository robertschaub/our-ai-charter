# SPDX-License-Identifier: AGPL-3.0-only
"""Editable vector masters for the simplified and detailed EGA diagrams.
Run with --figure cover (default) or --figure inline.
This script writes SVGs only; publication PNGs are exported separately.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[2] / 'docs' / 'Published'
INK = '#173146'

def text(x, y, value, size=32, color=INK, weight=400, anchor='start'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{escape(value)}</text>'

def rect(x,y,w,h,fill='#fff',stroke='none',r=24,sw=2,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'

def vector_tools(a):
    """Shared text, flat shapes and icon primitives for both diagrams."""
    navy, blue, teal, red, gold = '#10175E', '#086DD9', '#00A4BD', '#EA233B', '#F4B900'
    pale, mint, cream = '#EAF6FF', '#EDF9FB', '#FFF8E3'
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

    return label, box, line, arrow, icon


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

    label, box, line, arrow, icon = vector_tools(a)

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
    """Current detailed diagram; export at width 2400, preserving aspect ratio."""
    navy, blue, teal, red, gold = '#10175E', '#086DD9', '#00A4BD', '#EA233B', '#F4B900'
    pale, mint, cream = '#EAF6FF', '#EDF9FB', '#FFF8E3'

    a=['<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1064" viewBox="0 0 1536 1064" role="img" aria-labelledby="title desc">','<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->','<title id="title">Evidence-Gated Agents — the same check at each relevant boundary</title>','<desc id="desc">The full EGA design. Evidence sources feed a retrieval service available to every check. Working AI plans within existing permission, faces a check before this use, performs permitted work, and faces another check before release or action. Proceed permits the checked step and leads to an outcome record, with an optional return for further work. Either check can refuse the step. Do not proceed leads to remaining stopped and recording the reason, with an optional permitted revision and recheck route. Human judgement is conditional. Affected people, independent custody of decision records and five oversight roles remain visible. Crossing lines do not join.</desc>','<rect width="1536" height="1064" fill="white"/>','<g font-family="Arial, Helvetica, sans-serif">']
    label, box, line, arrow, icon = vector_tools(a)

    box(46,28,10,96,gold,'none',5)
    label(69,73,'Evidence-Gated Agents',51,bold=True)
    label(69,124,'Evidence before AI proceeds',34,bold=True)
    label(69,163,'The same check pattern at each relevant boundary',25,blue)

    box(68,188,390,152)
    label(88,224,'Evidence sources',30,bold=True)
    label(88,254,'Public and permitted private sources',20,blue)
    for kind,x in [('doc',108),('globe',192),('database',279),('lock',365)]:
        icon(kind,x,267,.88)
    arrow(458,260,531,260,teal,14,25)
    box(531,188,583,152)
    icon('doc',580,215,1.1)
    icon('search',650,246,.65)
    label(741,222,'Evidence service',30,bold=True)
    label(741,251,'Finds material on request',21,blue)
    label(741,278,'Sources and search coverage',21,blue)
    label(741,305,'Available to every EGA check',21,blue)
    line('M557 312 H1090',blue,1)
    label(823,331,'Evidence for claims, permissions and authority',18,blue,anchor='middle')

    # The two example boundaries request evidence from the same broad service.
    for xreq,xresult in [(534,575),(930,971)]:
        line(f'M{xreq} 400 V360',blue,6,'7 5')
        a.append(f'<polygon points="{xreq-11},360 {xreq},341 {xreq+11},360" fill="{blue}"/>')
        arrow(xresult,342,xresult,400,teal,11,21)
    label(506,368,'Request /',17,blue,anchor='end')
    label(506,389,'results',17,blue,anchor='end')
    label(992,368,'Request /',17,blue)
    label(992,389,'results',17,blue)

    box(68,402,162,196)
    icon('brain',111,416,1.13,teal)
    label(149,521,'Working AI',25,bold=True,anchor='middle')
    label(149,548,'Plan & prepare',20,blue,True,'middle')
    label(149,570,'Within existing',18,blue,anchor='middle')
    label(149,589,'permission',18,blue,anchor='middle')
    arrow(40,476,68,476,teal,14,24)
    arrow(230,476,269,476,teal,14,24)

    # Simple flat gold frames match the simplified cover.
    box(269,403,296,194,cream,gold,8,5)
    a.append(f'<g transform="translate(287 416) scale(.76)" fill="none" stroke="{gold}" stroke-width="3" stroke-linejoin="round"><path d="M32 3 L57 13 V34 Q57 53 32 66 Q7 53 7 34 V13 Z M32 17 V54 M21 29 H43 M21 41 H43"/></g>')
    label(355,444,'EGA check',29,bold=True)
    label(355,469,'Before this use',19,blue)
    for y,title,detail in [(479,'Authority','Purpose and scope'),(516,'Inputs','Origin, integrity and trust'),(553,'Data protection','Permitted processing')]:
        box(283,y,108,32,'#E1F2FF','none',5)
        box(396,y,156,32,'#E1F2FF','none',5)
        label(291,y+21,title,12.5,blue,True)
        label(403,y+21,detail,13,blue)
    arrow(565,476,599,476,teal,14,23)

    box(599,402,210,196)
    icon('brain',646,418,.95,teal)
    icon('doc',717,425,.79)
    label(704,522,'Working AI',27,bold=True,anchor='middle')
    label(704,551,'Carry out permitted work',17,blue,anchor='middle')
    label(704,575,'Propose the next step',18,blue,anchor='middle')
    arrow(809,476,838,476,teal,14,23)

    box(838,403,258,194,cream,gold,8,5)
    a.append(f'<g transform="translate(853 418) scale(.7)" fill="none" stroke="{gold}" stroke-width="3" stroke-linejoin="round"><path d="M32 3 L57 13 V34 Q57 53 32 66 Q7 53 7 34 V13 Z M32 17 V54 M21 29 H43 M21 41 H43"/></g>')
    label(914,443,'EGA check',28,bold=True)
    label(914,469,'Before release or action',15.5,blue)
    for y,title,details in [(479,'Evidence',['Support, contradiction','and gaps']),(519,'Authority',['Current mandate']),(556,'Disclosure',['Permitted content','and recipient'])]:
        h=35 if len(details)==2 else 32
        box(850,y,88,h,'#E1F2FF','none',5)
        box(942,y,142,h,'#E1F2FF','none',5)
        label(858,y+22,title,14,blue,True)
        for i,d in enumerate(details):
            label(949,y+(14 if len(details)==2 else 22)+i*15,d,12.5,blue)
    arrow(1096,476,1117,476,teal,13,20)

    box(1117,402,185,196,mint,teal)
    a.append(f'<circle cx="1155" cy="451" r="25" fill="{teal}"/>')
    line('M1143 451 L1152 460 L1169 441','white',6)
    label(1189,453,'Proceed',24,bold=True)
    label(1209,491,'Within checked scope',16,blue,anchor='middle')
    label(1209,527,'Carry out the',18,blue,anchor='middle')
    label(1209,552,'checked step',18,blue,anchor='middle')
    line('M1209 402 V202 H1308',teal,11)
    arrow(1308,202,1331,202,teal,11,22)
    icon('people',1344,157,1.66)
    label(1398,284,'People receiving or',19,blue,anchor='middle')
    label(1398,309,'affected by the result',19,blue,anchor='middle')
    arrow(1302,476,1327,476,teal,13,24)
    box(1327,435,194,78,'white',teal,29,3.5)
    icon('doc',1343,450,.68,teal)
    label(1395,470,'End · record',18,bold=True)
    label(1395,497,'outcome',20,bold=True)

    # Either refusal feeds the same stop branch. The exit stays straight.
    line('M499 598 V639 Q499 659 518 659 H540',red,12)
    arrow(539,659,559,659,red,12,20)
    line('M936 598 V617 Q936 636 920 636',red,12)
    arrow(924,636,904,636,red,12,20)
    box(559,622,345,78,'#FFF4F5',red,12)
    a.append(f'<circle cx="606" cy="661" r="27" fill="{red}"/>')
    line('M595 650 L617 672 M617 650 L595 672','white',6)
    label(648,654,'Do not proceed',26,bold=True)
    label(648,682,'Reason and permitted next route',15.5,blue)
    arrow(904,661,1282,661,red,10,24)
    box(1282,625,224,76,'white',red,26,3)
    icon('doc',1299,637,.77,red)
    label(1360,654,'Remain stopped',18,bold=True)
    label(1360,683,'Record reason',18,blue)

    # The dotted association has no arrowheads: human judgement is conditional.
    line('M904 680 Q938 710 979 716',blue,4,'3 7')
    icon('people',982,697,.90)
    label(1055,712,'Authorised human',17,blue)
    label(1055,734,'judgement',17,blue)
    label(1055,756,'Where needed',17,blue)

    line('M749 700 V722 Q749 742 728 742 H174 Q153 742 153 721 V618',blue,5,'12 7')
    a.append(f'<polygon points="141,618 153,598 165,618" fill="{blue}"/>')
    label(417,728,'Revise if permitted · recheck',22,blue,anchor='middle')
    # Break the dashed line at the solid exit, so the crossing is not a junction.
    line('M1239 598 V650',teal,5,'12 7')
    line('M1239 672 V760 Q1239 781 1218 781 H114 Q93 781 93 760 V618',teal,5,'12 7')
    a.append(f'<polygon points="81,618 93,598 105,618" fill="{teal}"/>')
    label(173,769,'Further work, if needed',21,teal)

    box(69,810,1437,188)
    label(84,844,'Human accountability and oversight',29,bold=True)
    for x in [83,365,647,929,1211]:
        box(x,858,276,79,'white',blue,8,1.5)
    # Deliberately simple native symbols match the cover's stroke style.
    a.append(f'<g transform="translate(100 873)" fill="none" stroke="{blue}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"><path d="M8 46 L37 17 M28 8 L45 25 M35 1 L53 19 M28 8 L35 1 M45 25 L53 19 M37 17 L44 10 M5 51 L13 51 M39 51 H63 M43 46 H59"/></g>')
    label(179,887,'Rulemaker',21,blue)
    label(179,917,'Sets criteria',18,blue)
    icon('person',388,869,.88)
    label(460,887,'Operator',21,blue)
    label(460,917,'Oversees operation',18,blue)
    icon('doc',668,869,.88)
    label(737,881,'Record keeper',20,blue)
    label(737,905,'Independent custody',17,blue)
    label(737,927,'of decision records',17,blue)
    icon('search',949,871,.85)
    label(1017,887,'Independent reviewer',18,blue)
    label(1017,917,'Assesses the basis',17,blue)
    a.append(f'<g transform="translate(1227 871)" fill="none" stroke="{blue}" stroke-width="3.5" stroke-linejoin="round"><path d="M34 2 V61 M22 61 H46 M6 12 H62 M11 12 L1 39 H21 Z M57 12 L47 39 H67 Z"/><circle cx="34" cy="12" r="4" fill="{blue}"/></g>')
    label(1307,887,'Remedy decider',19,blue)
    label(1307,917,'Acts within mandate',17,blue)
    box(83,943,1409,39,'white',blue,8,1.5)
    icon('lock',94,945,.48,navy)
    label(131,971,'Restricted decision records · Inspect · Challenge · Correct',20,blue)
    line('M69 1027 H620 M972 1027 H1506',blue,1.8)
    label(796,1034,'Data protection throughout',20,blue,anchor='middle')
    a.append('</g></svg>')
    (ROOT/'evidence-gated-agents-before-we-rely.svg').write_text('\n'.join(a),encoding='utf-8')

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--figure', choices=['cover', 'inline'], default='cover')
    args = parser.parse_args()
    (cover if args.figure == 'cover' else inline)()
