# SPDX-License-Identifier: AGPL-3.0-only
"""Build the public Evidence-Gated Agents action-path PDF."""

from math import hypot
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output" / "pdf" / "evidence-gated-agents-dynamic-decision-path.pdf"
TEMP = OUTPUT.with_name("evidence-gated-agents-action-path.rendering.pdf")
OVERVIEW_URL = "https://github.com/robertschaub/our-ai-charter/blob/main/docs/Assurance/Concepts/evidence-gated-agents.md"
W, H = landscape(A4)

NAVY = HexColor("#102A43")
INK = HexColor("#243B53")
MUTED = HexColor("#52606D")
PAPER = HexColor("#F7F9FC")
WHITE = HexColor("#FFFFFF")
LINE = HexColor("#CBD5E1")
BLUE = HexColor("#285D85")
BLUE_BG = HexColor("#EAF2FA")
TEAL = HexColor("#2C7A7B")
TEAL_BG = HexColor("#E6FFFA")
ORANGE = HexColor("#9C4600")
ORANGE_BG = HexColor("#FFF2E5")
RED = HexColor("#B54747")
RED_BG = HexColor("#FFF0F0")
GREEN = HexColor("#327A4D")
GREEN_BG = HexColor("#E8F5EC")


def fonts():
    pdfmetrics.registerFont(TTFont("Arial", r"C:\Windows\Fonts\arial.ttf"))
    pdfmetrics.registerFont(TTFont("Arial-Bold", r"C:\Windows\Fonts\arialbd.ttf"))


def lines(text, width, size=8, font="Arial"):
    result = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if not current or pdfmetrics.stringWidth(candidate, font, size) <= width:
                current = candidate
            else:
                result.append(current)
                current = word
        result.append(current)
    return result


def text(c, value, x, y, width, size=8, color=INK, bold=False, leading=None, centre=False):
    font = "Arial-Bold" if bold else "Arial"
    leading = leading or size * 1.25
    c.setFont(font, size)
    c.setFillColor(color)
    for row in lines(value, width, size, font):
        if centre:
            c.drawCentredString(x + width / 2, y, row)
        else:
            c.drawString(x, y, row)
        y -= leading
    return y


def card(c, x, y, w, h, title, body, fill=WHITE, stroke=LINE, title_color=None):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, 8, stroke=1, fill=1)
    text(c, title, x + 9, y + h - 18, w - 18, 8.2, title_color or stroke, True, 9.5, True)
    text(c, body, x + 9, y + h - 38, w - 18, 7.2, INK, False, 8.6, True)


def arrow(c, x1, y1, x2, y2, color=INK):
    c.setStrokeColor(color)
    c.setFillColor(color)
    c.setLineWidth(1.4)
    c.line(x1, y1, x2, y2)
    dx, dy = x2 - x1, y2 - y1
    length = hypot(dx, dy)
    ux, uy = dx / length, dy / length
    p = c.beginPath()
    p.moveTo(x2, y2)
    p.lineTo(x2 - 6 * ux - 3.5 * uy, y2 - 6 * uy + 3.5 * ux)
    p.lineTo(x2 - 6 * ux + 3.5 * uy, y2 - 6 * uy - 3.5 * ux)
    p.close()
    c.drawPath(p, fill=1, stroke=0)


def header(c, title, subtitle, label, page):
    c.setFillColor(PAPER)
    c.rect(0, 0, W, H, stroke=0, fill=1)
    text(c, title, 36, 555, 580, 22, NAVY, True, 24)
    text(c, subtitle, 36, 528, 620, 10, MUTED, False, 12)
    c.setFillColor(ORANGE_BG)
    c.setStrokeColor(ORANGE)
    c.roundRect(655, 536, 150, 29, 14, stroke=1, fill=1)
    text(c, label, 665, 553, 130, 7.5, ORANGE, True, 9, True)
    c.setFillColor(MUTED)
    c.setFont("Arial", 6.8)
    c.drawRightString(805, 14, f"Evidence-Gated Agents | 2026-09-30 | {page} of 2")
    c.setFillColor(BLUE)
    c.drawString(36, 14, "Source: Evidence-Gated Agents overview (authoritative Markdown)")
    c.linkURL(OVERVIEW_URL, (36, 12, 240, 22), relative=0)


def page_prototype(c):
    header(
        c,
        "Selected prototype: dynamic decision examination",
        "A preset rule routes consequential decisions or instructions to act into the gate.",
        "PLANNED INTEGRATION",
        1,
    )

    text(c, "Integration not implemented. Trigger fixtures, routing-record schema, API contract, release rule and Runtime compatibility remain open.", 36, 503, 770, 8.5, MUTED)

    y, h = 397, 83
    nodes = [
        (36, 128, "REQUEST", "Free request plus permitted relevant context", BLUE_BG, BLUE),
        (186, 138, "NORMAL AI AGENT", "Proposes one exact response", BLUE_BG, BLUE),
        (347, 174, "PRESET TRIGGER RULE", "Does the response contain a consequential decision or an instruction to act?", ORANGE_BG, ORANGE),
        (578, 228, "ORDINARY ANSWER", "Release answer + minimal routing record.\nNo receipt; no request or response content retained in the record.", BLUE_BG, BLUE),
    ]
    for x, width, title, body, fill, stroke in nodes:
        card(c, x, y, width, h, title, body, fill, stroke)
    for left, right in zip(nodes, nodes[1:]):
        arrow(c, left[0] + left[1] + 2, y + h / 2, right[0] - 2, y + h / 2)

    text(c, "No", 535, 449, 30, 8, BLUE, True)
    text(c, "Yes", 443, 384, 35, 8, ORANGE, True)
    c.setStrokeColor(INK)
    c.setLineWidth(1.4)
    c.line(434, 395, 434, 374)
    c.line(434, 374, 100, 374)
    arrow(c, 100, 374, 100, 353)

    y, h = 265, 86
    nodes = [
        (36, 128, "AUTHORIZE + SUBMIT", "Authority and disclosure checks for this release", ORANGE_BG, ORANGE),
        (186, 152, "FACTHARBOR", "Evidence search and analysis; verdict + report with support, counterevidence, limits and uncertainty", TEAL_BG, TEAL),
        (367, 125, "VERIFY: EGA RULE", "Does the completed result sufficiently support the exact decision?", ORANGE_BG, ORANGE),
        (521, 124, "COMMIT", "Recheck bound request, decision, recipient and evidence result", GREEN_BG, GREEN),
        (674, 132, "RELEASE", "Release only the checked decision + release receipt", GREEN_BG, GREEN),
    ]
    for x, width, title, body, fill, stroke in nodes:
        card(c, x, y, width, h, title, body, fill, stroke)
    for left, right in zip(nodes, nodes[1:]):
        arrow(c, left[0] + left[1] + 2, y + h / 2, right[0] - 2, y + h / 2)
    text(c, "Pass", 164, 319, 22, 6.4, INK, centre=True)
    text(c, "Pass", 492, 319, 29, 6.4, INK, centre=True)

    card(c, 36, 180, 770, 53, "STOP + RECEIPT", "Failed authority/disclosure, pending analysis, contradiction, insufficient evidence, ambiguity or technical error. Completion cannot release later; a retry starts a new attempt through all checks.", RED_BG, RED)
    arrow(c, 100, y - 2, 100, 235, RED)
    arrow(c, 429.5, y - 2, 429.5, 235, RED)
    text(c, "Fail", 110, 246, 40, 7, RED)
    text(c, "Fail / unclear / error", 439, 246, 125, 7, RED)

    text(c, "WHAT IS PRESET AND WHAT IS DYNAMIC", 36, 159, 500, 10, NAVY, True)
    card(c, 36, 76, 360, 68, "PRESET FOR THE PROTOTYPE", "Trigger rule; data and disclosure boundaries; recipient and release contract; controlled German/English requests. Release rule and routing/receipt schemas remain open preparation work.", WHITE, BLUE)
    card(c, 414, 76, 392, 68, "DYNAMIC FOR GATED ATTEMPTS", "Exact decision; permitted context; one new FactHarbor analysis; supporting and opposing evidence; limits and uncertainty; release or stop outcome. Ordinary answers use only the routing record.", WHITE, TEAL)

    text(c, "BOUNDARY", 36, 56, 80, 7.5, ORANGE, True)
    text(c, "The gated path releases a checked decision. It does not execute or authorize a resulting action. Controlled tests select one clear, non-complex decision.", 112, 56, 694, 7.4, INK, False, 9)


def page_product(c):
    header(
        c,
        "Later EGA: repeat control at every effect boundary",
        "A released decision does not itself authorize a message, tool call, filing, payment or system change.",
        "LATER DEVELOPMENT",
        2,
    )

    y, h = 355, 80
    nodes = [
        (36, 115, "REQUEST", "One task may lead to several decisions", BLUE_BG, BLUE),
        (173, 125, "DECISIONS", "Check evidence and release each exact decision", TEAL_BG, TEAL),
        (320, 130, "PROPOSED EFFECT", "Message, tool call, filing, payment or change", ORANGE_BG, ORANGE),
        (472, 140, "AUTHORIZE AGAIN", "Is this agent system allowed to make this effect now?", ORANGE_BG, ORANGE),
        (634, 172, "EXECUTE + RECORD", "Bind the exact effect, execute once, and record the actual outcome", GREEN_BG, GREEN),
    ]
    for x, width, title, body, fill, stroke in nodes:
        card(c, x, y, width, h, title, body, fill, stroke)
    for left, right in zip(nodes, nodes[1:]):
        arrow(c, left[0] + left[1] + 2, y + h / 2, right[0] - 2, y + h / 2)

    card(c, 472, 248, 334, 60, "NO AUTHORITY OR FAILED CHECK", "Stop the effect and create a receipt. Earlier decision approval does not carry forward.", RED_BG, RED)
    c.setStrokeColor(RED)
    c.setLineWidth(1.3)
    c.line(542, y - 2, 542, 310)
    c.setFillColor(RED)
    c.circle(542, 310, 3, stroke=0, fill=1)

    text(c, "SELECTED PROTOTYPE", 36, 218, 250, 10, NAVY, True)
    text(c, "LATER PRODUCT WORK", 430, 218, 300, 10, NAVY, True)
    card(c, 36, 84, 350, 115, "ONE CONTROLLED DECISION RELEASE", "Preset trigger; ordinary answers bypass with a routing record, not a receipt. Gated decisions use dynamic FactHarbor examination, exact Commit binding and a release or stop receipt. Integration is planned; resulting actions remain outside scope.", WHITE, BLUE)
    card(c, 430, 84, 376, 115, "MULTIPLE DECISIONS AND EFFECTS", "Organisational identity and delegation; private permitted evidence; fresh control at agent and tool hand-offs; effect-specific authorization; lifecycle, recovery, challenge and accountable remedy.", WHITE, ORANGE)

    text(c, "KNOWN LIMIT", 36, 62, 90, 7.5, RED, True)
    text(c, "FactHarbor's model-assisted decomposition can miss a consequential decision component. The prototype evaluates and reports this; it does not claim complete semantic coverage.", 126, 62, 680, 7.4, INK, False, 9)


def metadata():
    reader = PdfReader(str(TEMP))
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.root_object[NameObject("/Lang")] = TextStringObject("en")
    writer.add_metadata(
        {
            "/Title": "Evidence-Gated Agents - selected prototype and later action path",
            "/Subject": "Preset routing and dynamic decision examination in the planned prototype; later effect authorization",
            "/Author": "Robert Schaub - FactHarbor Verein",
        }
    )
    with OUTPUT.open("wb") as stream:
        writer.write(stream)
    TEMP.unlink()


def build_pdf():
    fonts()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    c = canvas.Canvas(str(TEMP), pagesize=(W, H), pageCompression=1)
    c.setCreator("ReportLab")
    page_prototype(c)
    c.showPage()
    page_product(c)
    c.showPage()
    c.save()
    metadata()


if __name__ == "__main__":
    build_pdf()
