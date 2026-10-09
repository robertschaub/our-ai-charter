# SPDX-License-Identifier: AGPL-3.0-only
"""Shared current EGA overview and historical detailed article figure.
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
            'gavel':'<path d="M8 46 L37 17 M28 8 L45 25 M35 1 L53 19 M28 8 L35 1 M45 25 L53 19 M37 17 L44 10 M5 51 L13 51 M39 51 H63 M43 46 H59"/>',
            'scales':'<path d="M34 2 V61 M22 61 H46 M6 12 H62 M11 12 L1 39 H21 Z M57 12 L47 39 H67 Z"/><circle cx="34" cy="12" r="4" fill="currentColor"/>',
            'people':'<circle cx="32" cy="14" r="10"/><circle cx="10" cy="24" r="7"/><circle cx="54" cy="24" r="7"/><path d="M16 60 V43 A16 16 0 0 1 48 43 V60 Z M16 39 C4 32 0 43 0 50 V60 H16 M48 39 C60 32 64 43 64 50 V60 H48"/>',
            'shield':'<path d="M32 3 L57 13 V34 Q57 53 32 66 Q7 53 7 34 V13 Z" fill="currentColor" stroke="none"/><path d="M20 33 L29 42 L45 24" stroke="white"/>',
            'brain':'<path d="M32 10 C17 -2 6 9 10 20 C-2 24 1 38 10 42 C0 55 14 68 28 60 M32 10 C47 -2 58 9 54 20 C66 24 63 38 54 42 C64 55 50 68 36 60 M32 8 V63 M10 20 Q24 17 22 31 M10 42 Q24 42 20 54 M54 20 Q40 17 42 31 M54 42 Q40 42 44 54"/>',
        }
        a.append(f'<g transform="translate({x} {y}) scale({scale})" color="{color}" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round" stroke-linejoin="round">{shapes[kind]}</g>')

    return label, box, line, arrow, icon


def cover():
    """Canonical overview for the public pages and independent documentation copies.

    Optional PNG exports must preserve the SVG aspect ratio.
    Edit these coordinates rather than painting over a previously exported PNG.
    """
    navy, blue, teal, red, gold = '#10175E', '#086DD9', '#00A4BD', '#EA233B', '#F4B900'
    pale, mint, cream = '#EAF6FF', '#EDF9FB', '#FFF8E3'
    a = [f'<svg xmlns="http://www.w3.org/2000/svg" width="1680" height="1195" viewBox="0 0 1680 1195" role="img" aria-labelledby="title desc">',
         '<!-- SPDX-License-Identifier: CC-BY-SA-4.0 -->',
         '<title id="title">Evidence-Gated Agents — evidence before AI proceeds</title>',
         '<desc id="desc">Proposed wider design. Working AI plans within existing permission and proposes a step to an EGA check selected by trusted rules. Evidence sources feed a retrieval service; EGA assesses the material. Proceed permits only the checked step. Do not proceed keeps the step blocked, including while pending. Both branches feed one decision record and receipt, including actual or uncertain outcomes if attempted. Further work or revision requires permission and fresh applicable checks; uncertain effects require reconciliation before any potentially duplicating attempt. Human judgement informs the blocked branch without replacing evidence or authority. People receiving or affected by results and human accountability remain visible. Crossing lines do not join.</desc>',
         '<rect width="1680" height="1195" fill="white"/>',
         '<g font-family="Arial, Helvetica, sans-serif">']

    label, box, line, arrow, icon = vector_tools(a)

    # Header and all content share the accepted left margin.
    box(58,28,10,99,gold,'none',5)
    label(86,76,'Evidence-Gated Agents',60,bold=True)
    label(86,126,'Evidence before AI proceeds',40,bold=True)
    label(86,164,'One check, repeated whenever needed',26,blue)

    a.append('<g transform="translate(-30 0)">')
    box(88,188,404,170)
    label(290,227,'Evidence sources',32,bold=True,anchor='middle')
    label(290,260,'Public and permitted private sources',22,blue,anchor='middle')
    for kind,x in [('doc',141),('globe',225),('database',308),('lock',389)]:
        icon(kind,x,280,.92)
    a.append('</g>')
    arrow(462,282,505,282,head=24)
    a.append('<g transform="translate(-70 0)">')
    box(575,188,415,170)
    label(782.5,227,'Evidence service',32,bold=True,anchor='middle')
    label(782.5,255,'Finds permitted material',21,blue,anchor='middle')
    label(782.5,281,'Reports sources and search coverage',21,blue,anchor='middle')
    label(782.5,307,'For claims, permissions and authority',20,blue,anchor='middle')
    icon('doc',744,320,.4)
    icon('search',798,320,.4)

    # Evidence request and result lanes stay separate.
    line('M735 397 V375',blue,7,'6 4')
    a.append(f'<polygon points="724,376 735,358 746,376" fill="{blue}"/>')
    arrow(840,358,840,400,blue,10,19)
    label(708,385,'Request',18,bold=True,anchor='end')
    label(866,385,'Results',18,bold=True)
    a.append('</g>')

    a.append('<g transform="translate(-30 0)">')
    box(88,438,320,216)
    label(248,480,'Working AI',34,bold=True,anchor='middle')
    label(248,515,'Plans and proposes',26,blue,True,'middle')
    label(248,549,'Within existing permission',23,blue,anchor='middle')
    icon('brain',158,567,1.1,teal)
    icon('doc',276,566,1.08)
    # Same centreline, shaft width and arrowhead for entry and proposal.
    arrow(46,541,88,541)
    a.append('</g>')
    arrow(378,541,505,541)
    label(442,484,'Proposed',24,teal,True,'middle')
    label(442,515,'next step',24,teal,True,'middle')

    a.append('<g transform="translate(-70 0)">')
    box(575,401,415,367,cream,gold,14,6)
    label(782.5,447,'EGA check',36,bold=True,anchor='middle')
    label(782.5,477,'Before use, release or action',23,blue,anchor='middle')
    for yy,kind,title,details in [
        (486,'people','Authority',['Current mandate,','purpose and scope']),
        (558,'doc','Inputs',['Origin, integrity and trust']),
        (613,'search','Evidence',['Support, contradiction,','uncertainty and gaps']),
        (685,'shield','Permissions',['Access, processing and disclosure']),
    ]:
        box(594,yy,377,68 if len(details)>1 else 51,'#E1F2FF','none',10)
        icon(kind,613,yy+7,.62)
        label(674,yy+23,title,22,blue,True)
        for n,detail in enumerate(details):
            label(674,yy+44+n*20,detail,18,blue)
    label(782.5,759,'Trusted rules select checks for this step',18,blue,anchor='middle')
    a.append('</g>')

    arrow(920,466,1025,466,teal,14,24)
    arrow(920,618,1025,618,red,14,24)
    a.append('<g transform="translate(-45 0)">')
    box(1070,412,330,106,mint,teal)
    a.append(f'<circle cx="1125" cy="465" r="37" fill="{teal}"/>')
    line('M1108 466 L1121 479 L1144 451','white',9)
    label(1180,453,'Proceed',33,bold=True)
    label(1180,483,'Within checked scope',20,blue)
    label(1180,508,'Carry out the checked step',17,blue)
    a.append('</g>')

    # Release has a recipient; the wider affected group is a separate association.
    box(1100,188,310,102,mint,teal)
    label(1255,230,'Permitted recipient',25,bold=True,anchor='middle')
    label(1255,267,'Checked content only',22,blue,anchor='middle')
    arrow(1331,412,1331,290,teal,12,26)
    line('M1410 238 H1475',blue,3,'3 5')
    icon('people',1490,190,1.65)
    label(1545,310,'People receiving or',21,blue,anchor='middle')
    label(1545,338,'affected by the result',21,blue,anchor='middle')
    label(1310,335,'On confirmed output',19,blue,anchor='end')
    label(1310,360,'release',19,blue,anchor='end')
    arrow(1355,466,1428,466,teal,14,27)
    # One logical record for both branches, retaining the cover's right-hand layout.
    box(1428,427,212,232,pale,blue,18,2)
    label(1534,461,'Decision record',22,bold=True,anchor='middle')
    label(1534,492,'/ receipt',22,bold=True,anchor='middle')
    label(1534,535,'Reason or pending status',17,blue,anchor='middle')
    label(1534,572,'If attempted:',19,blue,anchor='middle')
    label(1534,603,'actual or uncertain',18,blue,anchor='middle')
    label(1534,631,'outcome',19,blue,anchor='middle')

    a.append('<g transform="translate(-45 0)">')
    box(1070,573,330,106,'#FFF4F5',red)
    a.append(f'<circle cx="1125" cy="620" r="32" fill="{red}"/>')
    line('M1111 606 L1139 634 M1139 606 L1111 634','white',8)
    label(1180,607,'Do not proceed',27,bold=True)
    label(1180,638,'Keep the step blocked',19,blue)
    label(1180,665,'No or pending',19,blue)
    a.append('</g>')
    arrow(1355,620,1428,620,red,10,25)

    # Judgement points into the blocked outcome, never into an exit or override.
    line('M1245 718 Q1160 710 1105 680 L1093 658',blue,3,'3 5')
    a.append(f'<polygon points="1096,652 1080,652 1091,664" fill="{blue}"/>')
    icon('people',1245,700,.8)
    label(1315,716,'Authorised human',22,blue)
    label(1315,744,'judgement',22,blue)
    label(1315,772,'Where needed',22,blue)

    # Optional returns enter Working AI from its bottom edge.
    line('M1080 679 V777 Q1080 796 1061 796 H934',blue,5,'12 7')
    line('M616 796 H229 Q210 796 210 777 V675',blue,5,'12 7')
    a.append(f'<polygon points="197,675 210,654 223,675" fill="{blue}"/>')
    label(780,804,'Revise if permitted · recheck',23,blue,anchor='middle')
    # Return starts at the checkmark; gaps cross refusal and revision without joining.
    line('M1080 502 V526 Q1080 536 1070 536 H985 Q975 536 975 546 V606',teal,5,'12 7')
    line('M975 630 V786 M975 806 V835 Q975 856 954 856 H945',teal,5,'12 7')
    line('M655 856 H158 Q136 856 136 834 V675',teal,5,'12 7')
    a.append(f'<polygon points="123,675 136,654 149,675" fill="{teal}"/>')
    label(800,864,'Further work, if permitted',23,teal,anchor='middle')

    # These are continuing responsibilities, not additional workflow gates.
    box(58,882,1582,250)
    label(74,918,'Human accountability and oversight',29,bold=True)
    responsibilities = [
        ('Rulemaker','gavel',['Sets criteria and','permitted scope']),
        ('Operator','person',['Oversees operation','and follows the rules']),
        ('Record keeper','locked_doc',['Provides independent','custody of decision','records']),
        ('Independent reviewer','search',['Examines the basis','and handling of','decisions']),
        ('Remedy decider','scales',['Decides corrections','or remedies within','mandate']),
    ]
    for n,(title,kind,lines) in enumerate(responsibilities):
        x=74+n*312
        box(x,935,302,135,'white',blue,8,1.5)
        icon(kind,x+14,957,.65)
        label(x+68,963,title,21,blue,True)
        for row,value in enumerate(lines):
            label(x+68,997+row*27,value,20,blue)
    box(74,1080,1550,38,'white',blue,8,1.5)
    icon('lock',84,1083,.43,navy)
    label(123,1107,'Restricted decision records · Inspect · Challenge · Seek correction',23,blue)
    line('M58 1171 H681 M1000 1171 H1640',blue,2)
    label(841,1178,'Data protection throughout',24,blue,anchor='middle')
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
