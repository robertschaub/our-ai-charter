# SPDX-License-Identifier: CC-BY-4.0
"""Build the public-safe Prototype Fund supplementary action-path PDF."""

from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT = REPO_ROOT / "output" / "pdf" / "evidence-gated-agents-action-path.pdf"
TEMP_OUTPUT = OUTPUT.with_name("evidence-gated-agents-action-path.rendering.pdf")

PAGE_W, PAGE_H = landscape(A4)

NAVY = HexColor("#102A43")
NAVY_2 = HexColor("#243B53")
INK = HexColor("#1F2933")
MUTED = HexColor("#52606D")
LINE = HexColor("#CBD5E1")
PAPER = HexColor("#F7F9FC")
WHITE = HexColor("#FFFFFF")
ORANGE = HexColor("#9C4600")
ORANGE_PALE = HexColor("#FFF2E5")
TEAL = HexColor("#2C7A7B")
TEAL_PALE = HexColor("#E6FFFA")
RED = HexColor("#B54747")
RED_PALE = HexColor("#FFF0F0")
BLUE = HexColor("#285D85")
BLUE_PALE = HexColor("#EAF2FA")
GRAY = HexColor("#64748B")
GRAY_PALE = HexColor("#EEF2F6")
GREEN = HexColor("#327A4D")
GREEN_PALE = HexColor("#E8F5EC")
PURPLE = HexColor("#6B5B95")
PURPLE_PALE = HexColor("#F2EFF8")


def register_fonts():
    pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))


def text_width(text, font="Arial", size=10):
    return pdfmetrics.stringWidth(text, font, size)


def wrapped_lines(text, max_width, font="Arial", size=10):
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for word in words[1:]:
            candidate = f"{current} {word}"
            if text_width(candidate, font, size) <= max_width:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return lines


def draw_text(
    c,
    text,
    x,
    y,
    width,
    font="Arial",
    size=10,
    color=INK,
    leading=None,
    align="left",
):
    leading = leading or size * 1.25
    c.setFont(font, size)
    c.setFillColor(color)
    lines = wrapped_lines(text, width, font, size)
    cursor_y = y
    for line in lines:
        if align == "center":
            c.drawCentredString(x + width / 2, cursor_y, line)
        elif align == "right":
            c.drawRightString(x + width, cursor_y, line)
        else:
            c.drawString(x, cursor_y, line)
        cursor_y -= leading
    return cursor_y


def rounded_card(
    c,
    x,
    y,
    w,
    h,
    fill=WHITE,
    stroke=LINE,
    radius=9,
    line_width=1,
    dashed=False,
):
    c.setLineWidth(line_width)
    c.setStrokeColor(stroke)
    c.setFillColor(fill)
    c.setDash(5, 3) if dashed else c.setDash()
    c.roundRect(x, y, w, h, radius, stroke=1, fill=1)
    c.setDash()


def arrow(c, x1, y1, x2, y2, color=NAVY_2, width=1.6, head=6, dashed=False):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(width)
    c.setDash(5, 3) if dashed else c.setDash()
    c.line(x1, y1, x2, y2)
    c.setDash()
    if abs(x2 - x1) >= abs(y2 - y1):
        direction = 1 if x2 >= x1 else -1
        points = [
            x2,
            y2,
            x2 - direction * head,
            y2 + head * 0.55,
            x2 - direction * head,
            y2 - head * 0.55,
        ]
    else:
        direction = 1 if y2 >= y1 else -1
        points = [
            x2,
            y2,
            x2 + head * 0.55,
            y2 - direction * head,
            x2 - head * 0.55,
            y2 - direction * head,
        ]
    path = c.beginPath()
    path.moveTo(points[0], points[1])
    path.lineTo(points[2], points[3])
    path.lineTo(points[4], points[5])
    path.close()
    c.drawPath(path, stroke=0, fill=1)


def poly_arrow(c, points, color=NAVY_2, width=1.5, head=6, dashed=False):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(width)
    c.setDash(5, 3) if dashed else c.setDash()
    path = c.beginPath()
    path.moveTo(*points[0])
    for point in points[1:]:
        path.lineTo(*point)
    c.drawPath(path, stroke=1, fill=0)
    c.setDash()
    x1, y1 = points[-2]
    x2, y2 = points[-1]
    if abs(x2 - x1) >= abs(y2 - y1):
        direction = 1 if x2 >= x1 else -1
        tip = [
            x2,
            y2,
            x2 - direction * head,
            y2 + head * 0.55,
            x2 - direction * head,
            y2 - head * 0.55,
        ]
    else:
        direction = 1 if y2 >= y1 else -1
        tip = [
            x2,
            y2,
            x2 + head * 0.55,
            y2 - direction * head,
            x2 - head * 0.55,
            y2 - direction * head,
        ]
    head_path = c.beginPath()
    head_path.moveTo(tip[0], tip[1])
    head_path.lineTo(tip[2], tip[3])
    head_path.lineTo(tip[4], tip[5])
    head_path.close()
    c.drawPath(head_path, stroke=0, fill=1)


def pill(c, text, x, y, w, h, fill, color, font_size=8):
    c.setFillColor(fill)
    c.setStrokeColor(fill)
    c.roundRect(x, y, w, h, h / 2, stroke=0, fill=1)
    c.setFillColor(color)
    c.setFont("Arial-Bold", font_size)
    c.drawCentredString(x + w / 2, y + (h - font_size) / 2 + 2, text)


def draw_gate(c, number, title, subtitle, x, y, w, h):
    rounded_card(
        c,
        x,
        y,
        w,
        h,
        fill=ORANGE_PALE,
        stroke=HexColor("#EAB27C"),
        radius=6,
        line_width=1,
    )
    pill(
        c,
        str(number),
        x + (w - 13) / 2,
        y + h - 16,
        13,
        13,
        ORANGE,
        WHITE,
        6.8,
    )
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 8)
    c.drawCentredString(x + w / 2, y + 18, title)
    c.setFillColor(MUTED)
    c.setFont("Arial", 7.2)
    c.drawCentredString(x + w / 2, y + 6, subtitle)


def draw_description_column(c, heading, body, x, y, width, heading_color):
    c.setFillColor(heading_color)
    c.setFont("Arial-Bold", 8.3)
    c.drawString(x, y, heading)
    return draw_text(
        c,
        body,
        x,
        y - 14,
        width,
        font="Arial",
        size=7.8,
        color=INK,
        leading=9.7,
    )


def draw_stage_card(c, x, y, w, h, heading, body, fill, stroke):
    rounded_card(c, x, y, w, h, fill=fill, stroke=stroke, radius=9, line_width=1)
    c.setFillColor(stroke)
    c.setFont("Arial-Bold", 8.4)
    c.drawString(x + 12, y + h - 20, heading)
    draw_text(
        c,
        body,
        x + 12,
        y + h - 38,
        w - 24,
        font="Arial",
        size=7.6,
        color=INK,
        leading=9.4,
    )


def draw_flow_node(c, x, y, w, h, title, subtitle, fill, stroke, dashed=False):
    rounded_card(
        c,
        x,
        y,
        w,
        h,
        fill=fill,
        stroke=stroke,
        radius=6,
        line_width=0.9,
        dashed=dashed,
    )
    draw_text(
        c,
        title,
        x + 5,
        y + h - 16,
        w - 10,
        font="Arial-Bold",
        size=7.2,
        color=stroke,
        leading=8.0,
        align="center",
    )
    draw_text(
        c,
        subtitle,
        x + 5,
        y + 13,
        w - 10,
        font="Arial",
        size=6.6,
        color=MUTED,
        leading=7.3,
        align="center",
    )


def draw_bridge_page(c):
    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 23)
    c.drawString(36, 554, "From a bounded prototype to a later product")
    c.setFillColor(NAVY_2)
    c.setFont("Arial", 10)
    c.drawString(
        36,
        532,
        "If funded, the prototype would test a control contract that a later product could retain while broadening its coverage.",
    )
    rounded_card(
        c,
        592,
        535,
        214,
        32,
        fill=ORANGE_PALE,
        stroke=HexColor("#EAB27C"),
        radius=16,
        line_width=0.8,
    )
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 8.2)
    c.drawCentredString(699, 553, "CAPABILITY EVOLUTION")
    c.setFillColor(MUTED)
    c.setFont("Arial", 7.1)
    c.drawCentredString(699, 542, "possible direction - not a committed roadmap")

    stage_y, stage_h, stage_w = 449, 62, 176
    stage_xs = [36, 234, 432, 630]
    draw_stage_card(
        c,
        stage_xs[0],
        stage_y,
        stage_w,
        stage_h,
        "TODAY",
        "FactHarbor Alpha and Our AI Charter Runtime PoC exist separately.",
        GRAY_PALE,
        GRAY,
    )
    draw_stage_card(
        c,
        stage_xs[1],
        stage_y,
        stage_w,
        stage_h,
        "IF FUNDED: BOUNDED PROTOTYPE",
        "Connect and evaluate one bounded German/English answer-release path.",
        BLUE_PALE,
        BLUE,
    )
    draw_stage_card(
        c,
        stage_xs[2],
        stage_y,
        stage_w,
        stage_h,
        "POSSIBLE LATER EXTENSIONS",
        "Select, scope and test each extension separately; no fixed order.",
        ORANGE_PALE,
        ORANGE,
    )
    draw_stage_card(
        c,
        stage_xs[3],
        stage_y,
        stage_w,
        stage_h,
        "LATER PRODUCT TARGET",
        "Apply retained controls to additional configured organisational action paths.",
        ORANGE_PALE,
        ORANGE,
    )

    arrow(c, 214, 480, 231, 480, color=BLUE, width=1.3, head=4.5)
    c.setFillColor(BLUE)
    c.setFont("Arial-Bold", 6.6)
    c.drawCentredString(223, 490, "BUILD")
    arrow(c, 412, 480, 429, 480, color=ORANGE, width=1.2, head=4.5, dashed=True)
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 6.3)
    c.drawCentredString(421, 490, "SCOPE")
    arrow(c, 610, 480, 627, 480, color=ORANGE, width=1.2, head=4.5, dashed=True)
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 6.2)
    c.drawCentredString(619, 490, "ADOPT")

    # Full operating picture for a possible later product.
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 10)
    c.drawString(36, 429, "POSSIBLE LATER PRODUCT - FULL OPERATING PICTURE")
    pill(c, "NOT FUNDED", 694, 420, 112, 18, ORANGE_PALE, ORANGE, 7.1)

    panel_x, panel_y, panel_w, panel_h = 36, 82, 770, 332
    rounded_card(c, panel_x, panel_y, panel_w, panel_h, fill=WHITE, stroke=HexColor("#EAB27C"), radius=10, line_width=1)

    # Organisation, authority and evidence remain outside the acting AI.
    org_x, org_y, org_w, org_h = 52, 354, 738, 44
    rounded_card(c, org_x, org_y, org_w, org_h, fill=ORANGE_PALE, stroke=ORANGE, radius=7, line_width=0.9)
    org_sections = [
        (org_x + 12, 220, "RESPONSIBLE ORGANISATION", "purpose, roles, operating envelope, review and remedy ownership"),
        (org_x + 258, 205, "AUTHORITY + POLICY", "scope, delegation, expiry, revocation and limits"),
        (org_x + 489, 237, "EVIDENCE SERVICE", "current assessment or separately governed acquisition"),
    ]
    for index, (x, width, title, body) in enumerate(org_sections):
        if index:
            c.setStrokeColor(HexColor("#EAB27C"))
            c.setLineWidth(0.6)
            c.line(x - 13, org_y + 8, x - 13, org_y + org_h - 8)
        c.setFillColor(ORANGE)
        c.setFont("Arial-Bold", 7.3)
        c.drawString(x, org_y + 27, title)
        draw_text(c, body, x, org_y + 14, width, font="Arial", size=6.7, color=INK, leading=7.3)

    main_y, main_h = 286, 50
    flow_nodes = [
        (52, 65, "QUESTION / TASK", "no answer or action released", WHITE, GRAY),
        (125, 80, "AUTHORIZE", "retained check, applied earlier", GREEN_PALE, GREEN),
        (213, 105, "PREPARE + SUBMIT", "later entry boundary; Submit rule retained", ORANGE_PALE, ORANGE),
        (326, 90, "ACTING AI", "uses admitted inputs; proposes only", BLUE_PALE, BLUE),
        (424, 100, "EXACT PROPOSAL", "frozen and withheld", GREEN_PALE, GREEN),
        (532, 105, "VERIFY + COMMIT", "supported and allowed to act?", GREEN_PALE, GREEN),
        (645, 145, "EXECUTOR -> EFFECT", "recheck retained; added effects need new tests", GREEN_PALE, GREEN),
    ]
    for x, width, title, body, fill, stroke in flow_nodes:
        draw_flow_node(c, x, main_y, width, main_h, title, body, fill, stroke)
    for left, right in zip(flow_nodes, flow_nodes[1:]):
        arrow(c, left[0] + left[1] + 1, main_y + main_h / 2, right[0] - 2, main_y + main_h / 2, color=NAVY_2, width=1.0, head=3.8)

    # Dependency rails: current authority and evidence feed the applicable checks.
    poly_arrow(c, [(410, org_y), (410, 345), (165, 345), (165, main_y + main_h)], color=BLUE, width=0.8, head=3.3, dashed=True)
    poly_arrow(c, [(410, org_y), (410, 341), (584, 341), (584, main_y + main_h)], color=BLUE, width=0.8, head=3.3, dashed=True)
    poly_arrow(c, [(665, org_y), (665, 349), (265, 349), (265, main_y + main_h)], color=TEAL, width=0.8, head=3.3, dashed=True)
    poly_arrow(c, [(665, org_y), (665, 345), (600, 345), (600, main_y + main_h)], color=TEAL, width=0.8, head=3.3, dashed=True)

    # A non-allow ruling stops or uses only a defined resolution route.
    stop_x, fresh_x, route_x, decision_y, decision_h = 52, 220, 388, 211, 51
    draw_flow_node(c, stop_x, decision_y, 150, decision_h, "DENY / TIMEOUT -> STOP", "recorded no-effect", RED_PALE, RED)
    draw_flow_node(c, fresh_x, decision_y, 150, decision_h, "FRESH PROPOSAL", "restart at Authorize; rerun all four checks", WHITE, PURPLE, dashed=True)
    rounded_card(c, route_x, decision_y, 402, decision_h, fill=PURPLE_PALE, stroke=PURPLE, radius=7, line_width=0.9)
    c.setFillColor(PURPLE)
    c.setFont("Arial-Bold", 7.3)
    c.drawString(route_x + 10, decision_y + 34, "ESCALATE - VALID OPTIONS INSIDE EXISTING AUTHORITY")
    c.setStrokeColor(HexColor("#B9AED3"))
    c.setLineWidth(0.6)
    c.line(route_x + 197, decision_y + 7, route_x + 197, decision_y + 31)
    c.setFillColor(INK)
    c.setFont("Arial-Bold", 7.0)
    c.drawString(route_x + 10, decision_y + 20, "AUTHORISED PERSON")
    draw_text(
        c,
        "NARROW -> fresh; DECLINE -> stop; no new authority or evidence",
        route_x + 10,
        decision_y + 10,
        182,
        font="Arial",
        size=6.6,
        color=INK,
        leading=7.1,
    )
    c.setFillColor(PURPLE)
    c.setFont("Arial-Bold", 7.0)
    c.drawString(route_x + 208, decision_y + 20, "FUTURE EXAMPLE ONLY - NOT FUNDED")
    draw_text(
        c,
        "machine issue -> candidate -> fresh; no new authority, evidence or release",
        route_x + 208,
        decision_y + 10,
        183,
        font="Arial",
        size=6.6,
        color=MUTED,
        leading=7.1,
    )
    arrow(c, route_x - 2, decision_y + decision_h / 2, fresh_x + 152, decision_y + decision_h / 2, color=PURPLE, width=0.9, head=3.5, dashed=True)

    # Collect non-allow outcomes from every gate, then show both possible routes.
    gate_centres = [165, 265, 584]
    c.setStrokeColor(MUTED)
    c.setLineWidth(0.7)
    for gate_x in gate_centres:
        c.line(gate_x, main_y, gate_x, 279)
    c.line(gate_centres[0], 279, gate_centres[-1], 279)
    pill(c, "ANY GATE: NON-ALLOW", 325, 272, 160, 14, WHITE, MUTED, 7.0)
    arrow(c, gate_centres[0], 279, stop_x + 75, decision_y + decision_h + 1, color=RED, width=0.8, head=3.2)
    arrow(c, gate_centres[-1], 279, route_x + 201, decision_y + decision_h + 1, color=PURPLE, width=0.8, head=3.2)

    # A changed or repaired candidate is a fresh proposal; approval never carries forward.
    poly_arrow(c, [(fresh_x + 75, decision_y + decision_h), (fresh_x + 75, 269), (165, 269), (165, main_y)], color=PURPLE, width=0.9, head=3.5, dashed=True)

    # Decline ends the path; only narrowing or a repair candidate yields a fresh proposal.
    poly_arrow(c, [(route_x + 99, decision_y), (route_x + 99, 201), (stop_x + 75, 201), (stop_x + 75, decision_y)], color=RED, width=0.9, head=3.5)
    pill(c, "DECLINE", 263, 195, 58, 13, WHITE, RED, 6.5)

    # Effect accountability continues after the executor acts.
    post_y, post_h = 135, 48
    post_nodes = [
        (52, 220, "ONGOING GOVERNANCE", "aggregate patterns may constrain, suspend or withdraw authority", ORANGE_PALE, ORANGE),
        (290, 220, "REVIEW / CHALLENGE", "inspect, correct or route remedy to an empowered owner", ORANGE_PALE, ORANGE),
        (528, 262, "OUTCOME + SCOPED RECEIPT", "exact proposal, basis, decision and outcome", GREEN_PALE, GREEN),
    ]
    for x, width, title, body, fill, stroke in post_nodes:
        draw_flow_node(c, x, post_y, width, post_h, title, body, fill, stroke)
    poly_arrow(c, [(717, main_y - 1), (798, main_y - 1), (798, post_y + post_h + 10), (659, post_y + post_h + 10), (659, post_y + post_h + 1)], color=GREEN, width=0.9, head=3.5)
    arrow(c, 527, post_y + post_h / 2, 512, post_y + post_h / 2, color=ORANGE, width=0.9, head=3.5)
    arrow(c, 289, post_y + post_h / 2, 274, post_y + post_h / 2, color=ORANGE, width=0.9, head=3.5)
    poly_arrow(c, [(52, post_y + post_h / 2), (44, post_y + post_h / 2), (44, org_y + org_h / 2), (52, org_y + org_h / 2)], color=ORANGE, width=0.9, head=3.5, dashed=True)

    # Two rules complete the multi-step product picture.
    rules_x, rules_y, rules_w, rules_h = 52, 88, 738, 31
    rounded_card(c, rules_x, rules_y, rules_w, rules_h, fill=GREEN_PALE, stroke=GREEN, radius=6, line_width=0.8)
    c.setStrokeColor(HexColor("#A8D5B7"))
    c.setLineWidth(0.6)
    c.line(rules_x + rules_w / 2, rules_y + 6, rules_x + rules_w / 2, rules_y + rules_h - 6)
    draw_text(c, "NEW MODEL / TOOL / AGENT HOP -> SUBMIT + VERIFY AGAIN", rules_x + 8, rules_y + 13, rules_w / 2 - 16, font="Arial-Bold", size=6.7, color=GREEN, align="center")
    draw_text(c, "EACH EXTERNAL EFFECT -> FRESH COMMIT + EXECUTOR CHECK", rules_x + rules_w / 2 + 8, rules_y + 13, rules_w / 2 - 16, font="Arial-Bold", size=6.7, color=GREEN, align="center")

    scope_x, scope_y, scope_w, scope_h = 36, 31, 770, 37
    rounded_card(
        c,
        scope_x,
        scope_y,
        scope_w,
        scope_h,
        fill=ORANGE_PALE,
        stroke=HexColor("#EAB27C"),
        radius=8,
        line_width=0.9,
    )
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 8.1)
    c.drawString(scope_x + 12, scope_y + 23, "SCOPE BOUNDARY")
    c.setFillColor(INK)
    c.setFont("Arial", 7.4)
    c.drawString(
        scope_x + 112,
        scope_y + 23,
        "Each later extension needs its own scope, implementation and evidence that it works.",
    )
    c.drawString(
        scope_x + 112,
        scope_y + 11,
        "None is a four-month commitment or part of a fixed delivery order.",
    )

    c.setFillColor(MUTED)
    c.setFont("Arial", 6.9)
    c.drawString(36, 10, "Grey: context/current foundation | Blue: acting AI/prototype | Green: retained control | Amber: organisational/later scope | Purple: non-allow resolution paths")
    c.drawRightString(806, 10, "Supplementary document | 2026-09-04 | 2 of 2")


def add_language_metadata(source, destination):
    reader = PdfReader(str(source))
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.root_object[NameObject("/Lang")] = TextStringObject("en")
    writer.add_metadata(
        {
            "/Title": "Evidence-Gated Agents - funded prototype and path to product",
            "/Subject": (
                "Funded prototype action path and a clearly separated path "
                "toward a possible later product"
            ),
            "/Author": "Robert Schaub - FactHarbor Verein",
        }
    )
    with destination.open("wb") as stream:
        writer.write(stream)
    source.unlink()


def build_pdf():
    register_fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    c = canvas.Canvas(
        str(TEMP_OUTPUT), pagesize=(PAGE_W, PAGE_H), pageCompression=1
    )
    c.setTitle("Evidence-Gated Agents - funded prototype and path to product")
    c.setSubject("Two-page funded prototype action path and path-to-product explanation")
    c.setAuthor("Robert Schaub - FactHarbor Verein")
    c.setCreator("ReportLab")

    c.setFillColor(PAPER)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # Header: one maturity statement, stated once.
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 23)
    c.drawString(36, 554, "Evidence-Gated Agents")
    c.setFont("Arial", 13)
    c.setFillColor(NAVY_2)
    c.drawString(36, 531, "Funded prototype action path")
    c.setFont("Arial", 9.4)
    c.setFillColor(MUTED)
    c.drawString(
        36,
        511,
        "FactHarbor prepares assessed claims. The acting AI drafts an exact proposal. A gateway outside that model decides release.",
    )
    rounded_card(
        c,
        588,
        535,
        217,
        32,
        fill=ORANGE_PALE,
        stroke=HexColor("#EAB27C"),
        radius=16,
        line_width=0.8,
    )
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 8.7)
    c.drawCentredString(696.5, 553, "FUNDED PROTOTYPE DESIGN")
    c.setFillColor(MUTED)
    c.setFont("Arial", 7.2)
    c.drawCentredString(
        696.5,
        542,
        "solid path only - not current end-to-end functionality",
    )

    # Funded path boundary.
    funded_x, funded_y, funded_w, funded_h = 36, 210, 770, 282
    rounded_card(
        c,
        funded_x,
        funded_y,
        funded_w,
        funded_h,
        fill=WHITE,
        stroke=HexColor("#D9A364"),
        radius=11,
        line_width=1.25,
    )
    pill(
        c,
        "FUNDED PROTOTYPE PATH",
        funded_x + 14,
        funded_y + funded_h - 28,
        148,
        18,
        ORANGE_PALE,
        ORANGE,
        7.7,
    )

    # Three visibly separate responsibility lanes.
    lane_x, lane_w, rail_w = 48, 746, 126

    # 1. FactHarbor prepares the evidence bundle before a covered request.
    fact_y, fact_h = 411, 45
    rounded_card(
        c,
        lane_x,
        fact_y,
        lane_w,
        fact_h,
        fill=TEAL_PALE,
        stroke=HexColor("#83C5BE"),
        radius=8,
        line_width=1,
    )
    c.setStrokeColor(HexColor("#B9DCD8"))
    c.setLineWidth(0.8)
    c.line(lane_x + rail_w, fact_y + 5, lane_x + rail_w, fact_y + fact_h - 5)
    c.setFillColor(TEAL)
    c.setFont("Arial-Bold", 8.7)
    c.drawString(58, 441, "FACTHARBOR")
    c.drawString(58, 430, "EVIDENCE WORK")
    c.setFillColor(MUTED)
    c.setFont("Arial", 7.2)
    c.drawString(58, 419, "before requests")

    fact_nodes = [
        (184, 122, "RETRIEVE PUBLIC SOURCES", "public material"),
        (326, 166, "ASSESS FIXED DE / EN CLAIMS", "verdicts; evidence for / against"),
        (514, 218, "PREPARED EVIDENCE BUNDLE", "current FactHarbor assessments"),
    ]
    for x, width, title, subtitle in fact_nodes:
        rounded_card(
            c,
            x,
            fact_y + 7,
            width,
            31,
            fill=WHITE,
            stroke=HexColor("#9ACBC6"),
            radius=6,
            line_width=0.8,
        )
        c.setFillColor(NAVY_2)
        c.setFont("Arial-Bold", 7.4)
        c.drawCentredString(x + width / 2, fact_y + 26, title)
        c.setFillColor(MUTED)
        c.setFont("Arial", 6.8)
        c.drawCentredString(x + width / 2, fact_y + 14, subtitle)
    arrow(c, 307, fact_y + 22.5, 324, fact_y + 22.5, color=TEAL, width=1, head=4)
    arrow(c, 493, fact_y + 22.5, 512, fact_y + 22.5, color=TEAL, width=1, head=4)

    # 2. The acting AI turns a covered request into an exact proposal; it cannot release.
    actor_y, actor_h = 351, 50
    rounded_card(
        c,
        lane_x,
        actor_y,
        lane_w,
        actor_h,
        fill=BLUE_PALE,
        stroke=HexColor("#9DBADA"),
        radius=8,
        line_width=1,
    )
    c.setStrokeColor(HexColor("#BDD0E4"))
    c.setLineWidth(0.8)
    c.line(lane_x + rail_w, actor_y + 5, lane_x + rail_w, actor_y + actor_h - 5)
    c.setFillColor(BLUE)
    c.setFont("Arial-Bold", 8.7)
    c.drawString(58, 384, "ACTING AI")
    c.drawString(58, 373, "REQUEST TO PROPOSAL")
    c.setFillColor(MUTED)
    c.setFont("Arial", 7.2)
    c.drawString(58, 361, "cannot decide release")

    request_x, request_y, request_w, request_h = 184, 360, 128, 32
    rounded_card(
        c,
        request_x,
        request_y,
        request_w,
        request_h,
        fill=WHITE,
        stroke=HexColor("#AFC7DF"),
        radius=6,
        line_width=0.8,
    )
    c.setFillColor(NAVY_2)
    c.setFont("Arial-Bold", 8)
    c.drawCentredString(request_x + request_w / 2, request_y + 18, "COVERED REQUEST")
    c.setFillColor(MUTED)
    c.setFont("Arial", 6.9)
    c.drawCentredString(request_x + request_w / 2, request_y + 7, "request-time input")

    draft_x, draft_y, draft_w, draft_h = 352, 358, 300, 36
    rounded_card(
        c,
        draft_x,
        draft_y,
        draft_w,
        draft_h,
        fill=WHITE,
        stroke=HexColor("#8FB2D2"),
        radius=6,
        line_width=0.9,
    )
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 8.3)
    c.drawCentredString(
        draft_x + draft_w / 2,
        draft_y + 21,
        "DRAFT / REDRAFT EXACT ANSWER PROPOSAL",
    )
    c.setFillColor(MUTED)
    c.setFont("Arial", 7.2)
    c.drawCentredString(
        draft_x + draft_w / 2,
        draft_y + 8,
        "Pinned acting model; no release decision",
    )
    arrow(
        c,
        request_x + request_w + 2,
        request_y + request_h / 2,
        draft_x - 2,
        request_y + request_h / 2,
        color=BLUE,
        width=1.2,
        head=4.5,
    )

    # The bundle supports drafting, while a separate branch feeds Verify directly.
    arrow(c, 624, fact_y + 7, 624, draft_y + draft_h + 1, color=TEAL, width=1.2, head=4.5)
    c.setFillColor(TEAL)
    c.setFont("Arial-Bold", 6.9)
    c.drawString(634, 402, "SELECTED ASSESSMENTS")

    # 3. The release gateway is outside the acting model.
    gateway_y, gateway_h = 220, 115
    rounded_card(
        c,
        lane_x,
        gateway_y,
        lane_w,
        gateway_h,
        fill=HexColor("#FFFBF6"),
        stroke=HexColor("#EAB27C"),
        radius=8,
        line_width=1,
    )
    c.setStrokeColor(HexColor("#F0C99F"))
    c.setLineWidth(0.8)
    c.line(lane_x + rail_w, gateway_y + 5, lane_x + rail_w, gateway_y + gateway_h - 5)
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 8.7)
    c.drawString(58, 320, "RELEASE GATEWAY")
    c.drawString(58, 309, "OUTSIDE ACTING AI")
    c.setFillColor(MUTED)
    c.setFont("Arial", 7.2)
    c.drawString(58, 297, "all four checks rerun")

    gate_y, gate_h, gate_w, gate_gap = 284, 44, 62, 10
    gate_xs = [284 + i * (gate_w + gate_gap) for i in range(4)]
    gates = [
        (1, "AUTHORIZE", "authority"),
        (2, "SUBMIT", "admissibility"),
        (3, "VERIFY", "evidence"),
        (4, "COMMIT", "exact draft"),
    ]
    for index, (number, title, subtitle) in enumerate(gates):
        draw_gate(c, number, title, subtitle, gate_xs[index], gate_y, gate_w, gate_h)
        if index < len(gates) - 1:
            arrow(
                c,
                gate_xs[index] + gate_w + 1,
                gate_y + gate_h / 2,
                gate_xs[index] + gate_w + gate_gap - 1,
                gate_y + gate_h / 2,
                color=ORANGE,
                width=1,
                head=3.3,
            )

    output_x, output_y, output_w, output_h = 590, 282, 192, 48
    rounded_card(
        c,
        output_x,
        output_y,
        output_w,
        output_h,
        fill=TEAL_PALE,
        stroke=HexColor("#83C5BE"),
        radius=7,
        line_width=1,
    )
    c.setFillColor(TEAL)
    c.setFont("Arial-Bold", 8.2)
    c.drawString(output_x + 10, output_y + 29, "RELEASE EXACT ANSWER + RECEIPT")
    c.setFillColor(INK)
    c.setFont("Arial", 6.9)
    c.drawString(
        output_x + 10,
        output_y + 12,
        "Answer  |  Authority  |  Basis  |  Decision  |  Outcome",
    )
    arrow(
        c,
        gate_xs[-1] + gate_w + 1,
        gate_y + gate_h / 2,
        output_x - 2,
        gate_y + gate_h / 2,
        color=TEAL,
        width=1.3,
        head=4.5,
    )
    c.setFillColor(TEAL)
    c.setFont("Arial-Bold", 6.9)
    c.drawCentredString(576, 318, "PASS")

    # Exact proposal enters at Authorize; every redraft follows this same route.
    poly_arrow(
        c,
        [
            (378, draft_y - 1),
            (378, 346),
            (gate_xs[0] + gate_w / 2, 346),
            (gate_xs[0] + gate_w / 2, gate_y + gate_h + 1),
        ],
        color=BLUE,
        width=1.2,
        head=4.5,
    )
    c.setFillColor(BLUE)
    c.setFont("Arial-Bold", 6.9)
    c.drawString(322, 338, "EXACT PROPOSAL")

    # The prepared bundle reaches Verify independently of the acting AI.
    poly_arrow(
        c,
        [
            (732, fact_y + 22.5),
            (748, fact_y + 22.5),
            (748, 333),
            (gate_xs[2] + gate_w / 2, 333),
            (gate_xs[2] + gate_w / 2, gate_y + gate_h + 1),
        ],
        color=TEAL,
        width=1.1,
        head=4.3,
    )
    c.setFillColor(TEAL)
    c.setFont("Arial-Bold", 6.8)
    c.drawRightString(771, 342, "ASSESSMENT BASIS - DIRECT TO VERIFY")

    # Any failed check enters STOP before either disposition. Individual drops
    # make it explicit that Authorize, Submit, Verify, and Commit can all fail.
    stop_x, stop_y, stop_w, stop_h = 352, 224, 164, 40
    gate_centers = [x + gate_w / 2 for x in gate_xs]
    fail_collector_y = 276
    c.setStrokeColor(RED)
    c.setLineWidth(1.0)
    for center_x in gate_centers:
        c.line(center_x, gate_y, center_x, fail_collector_y)
    c.line(gate_centers[0], fail_collector_y, gate_centers[-1], fail_collector_y)
    arrow(
        c,
        500,
        fail_collector_y,
        500,
        stop_y + stop_h,
        color=RED,
        width=1.2,
        head=4.5,
    )
    c.setFillColor(RED)
    c.setFont("Arial-Bold", 6.9)
    c.drawRightString(490, 266, "ANY CHECK FAILS")
    rounded_card(
        c,
        stop_x,
        stop_y,
        stop_w,
        stop_h,
        fill=RED_PALE,
        stroke=HexColor("#D99A9A"),
        radius=7,
        line_width=1,
    )
    c.setFillColor(RED)
    c.setFont("Arial-Bold", 8.6)
    c.drawCentredString(stop_x + stop_w / 2, stop_y + 25, "STOP - RELEASE BLOCKED")
    c.setFillColor(INK)
    c.setFont("Arial", 7)
    c.drawCentredString(stop_x + stop_w / 2, stop_y + 11, "Current exact proposal is not released")

    terminal_x, terminal_y, terminal_w, terminal_h = 184, 224, 142, 40
    rounded_card(
        c,
        terminal_x,
        terminal_y,
        terminal_w,
        terminal_h,
        fill=RED_PALE,
        stroke=HexColor("#D99A9A"),
        radius=7,
        line_width=0.9,
    )
    c.setFillColor(RED)
    c.setFont("Arial-Bold", 7.8)
    c.drawCentredString(terminal_x + terminal_w / 2, terminal_y + 25, "NO SAFE NARROWING")
    c.setFillColor(INK)
    c.setFont("Arial", 7)
    c.drawCentredString(terminal_x + terminal_w / 2, terminal_y + 14, "Current attempt ends")
    c.setFillColor(RED)
    c.setFont("Arial-Bold", 6.9)
    c.drawCentredString(terminal_x + terminal_w / 2, terminal_y + 5, "NO RELEASE")

    person_x, person_y, person_w, person_h = 542, 224, 166, 40
    rounded_card(
        c,
        person_x,
        person_y,
        person_w,
        person_h,
        fill=ORANGE_PALE,
        stroke=HexColor("#EAB27C"),
        radius=7,
        line_width=0.9,
    )
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 7.7)
    c.drawCentredString(person_x + person_w / 2, person_y + 26, "ESCALATE TO A PERSON")
    c.setFillColor(NAVY_2)
    c.setFont("Arial-Bold", 7)
    c.drawCentredString(person_x + person_w / 2, person_y + 15, "NARROW -> AI REDRAFT")
    c.setFillColor(RED)
    c.setFont("Arial-Bold", 6.7)
    c.drawCentredString(person_x + person_w / 2, person_y + 6, "DECLINE = REMAINS STOPPED")

    arrow(c, stop_x - 2, stop_y + 20, terminal_x + terminal_w + 2, terminal_y + 20, color=RED, width=1.1, head=4)
    c.setFillColor(MUTED)
    c.setFont("Arial", 7)
    c.drawCentredString(terminal_x + terminal_w / 2, 274, "not safely removable")
    arrow(c, stop_x + stop_w + 2, stop_y + 20, person_x - 2, person_y + 20, color=ORANGE, width=1.1, head=4)
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 6.7)
    c.drawCentredString(
        person_x + person_w / 2,
        274,
        "UNSUPPORTED PART SAFELY REMOVABLE",
    )

    # NARROW returns to the acting AI; DECLINE has no continuation.
    poly_arrow(
        c,
        [
            (person_x + person_w - 22, person_y + person_h),
            (787, person_y + person_h),
            (787, draft_y + draft_h / 2),
            (draft_x + draft_w + 2, draft_y + draft_h / 2),
        ],
        color=ORANGE,
        width=1.15,
        head=4.5,
    )
    c.setFillColor(ORANGE)
    c.setFont("Arial-Bold", 6.8)
    c.drawRightString(775, draft_y + draft_h / 2 + 7, "NARROW RETURNS TO ACTING AI")

    # Selectable explanatory text below the diagram.
    c.setStrokeColor(LINE)
    c.setLineWidth(0.8)
    c.line(36, 194, 806, 194)
    c.setFillColor(NAVY)
    c.setFont("Arial-Bold", 9.2)
    c.drawString(36, 179, "HOW TO READ THE DIAGRAM")

    column_y = 161
    draw_description_column(
        c,
        "FACTHARBOR + ACTING AI",
        (
            "Before a request, FactHarbor retrieves public sources, assesses fixed German "
            "and English claims, and prepares the evidence bundle. For a covered request, "
            "the acting AI uses selected assessments to draft or redraft the exact answer "
            "proposal. It cannot decide release."
        ),
        36,
        column_y,
        238,
        ORANGE,
    )
    draw_description_column(
        c,
        "GATEWAY, STOP AND DECLINE",
        (
            "The gateway outside the acting model checks authority, admissibility, evidence "
            "and the exact draft. Any failed check means STOP: no release. Only if the "
            "unsupported part can be removed safely may the gateway escalate to a person. "
            "NARROW returns to the acting AI for a fresh proposal; DECLINE keeps the current "
            "proposal stopped."
        ),
        301,
        column_y,
        238,
        RED,
    )
    draw_description_column(
        c,
        "RELEASE, RECEIPT AND RECHECK",
        (
            "Only the executing service can deliver the exact proposal after Commit. The "
            "recipient's receipt links the answer to its authority, basis, decision and "
            "outcome. A narrowed proposal is new: it returns to the acting AI, restarts at "
            "Authorize and reruns all four checks. No approval carries forward."
        ),
        566,
        column_y,
        240,
        TEAL,
    )

    c.setFillColor(MUTED)
    c.setFont("Arial", 6.9)
    c.drawString(36, 14, "Funded prototype path | Possible later extensions are shown on page 2")
    c.drawRightString(806, 14, "Supplementary document | 2026-09-04 | 1 of 2")

    c.showPage()
    draw_bridge_page(c)
    c.showPage()
    c.save()
    add_language_metadata(TEMP_OUTPUT, OUTPUT)


if __name__ == "__main__":
    build_pdf()
