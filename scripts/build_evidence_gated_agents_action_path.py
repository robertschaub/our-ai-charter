# SPDX-License-Identifier: CC-BY-4.0
"""Build the public Evidence-Gated Agents action-path PDF."""

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
    direction = 1 if x2 >= x1 else -1
    p = c.beginPath()
    p.moveTo(x2, y2)
    p.lineTo(x2 - direction * 6, y2 + 3.5)
    p.lineTo(x2 - direction * 6, y2 - 3.5)
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
    c.drawRightString(805, 14, f"Evidence-Gated Agents | 2026-09-16 | {page} of 2")


def page_prototype(c):
    header(
        c,
        "Selected prototype: dynamic decision examination",
        "A normal AI agent proposes the decision. FactHarbor examines its evidence. A separate gate decides release.",
        "SELECTED DIRECTION",
        1,
    )

    y, h = 366, 82
    nodes = [
        (36, 112, "1  REQUEST", "Free request plus permitted relevant context", BLUE_BG, BLUE),
        (168, 122, "2  NORMAL AI AGENT", "Proposes one exact decision; cannot release it", BLUE_BG, BLUE),
        (310, 116, "3  CHECKS", "Authority and disclosure for this release", ORANGE_BG, ORANGE),
        (446, 142, "4  FACTHARBOR", "One live examination: evidence for and against, limits and uncertainty", TEAL_BG, TEAL),
        (608, 92, "5  EGA RULE", "Sufficiently supported?", ORANGE_BG, ORANGE),
        (720, 86, "6  COMMIT", "Bind exact decision and recipient", GREEN_BG, GREEN),
    ]
    for x, width, title, body, fill, stroke in nodes:
        card(c, x, y, width, h, title, body, fill, stroke)
    for left, right in zip(nodes, nodes[1:]):
        arrow(c, left[0] + left[1] + 2, y + h / 2, right[0] - 2, y + h / 2)

    card(c, 574, 255, 214, 63, "RELEASE", "Only the exact checked decision is released. A release receipt records the path.", GREEN_BG, GREEN)
    card(c, 54, 255, 430, 63, "STOP", "Failed disclosure or authority, pending analysis, contradiction, insufficient evidence, ambiguity or technical error. A stop receipt is still created.", RED_BG, RED)
    arrow(c, 678, y - 2, 678, 320, GREEN)
    c.setStrokeColor(RED)
    c.setLineWidth(1.3)
    c.line(368, y - 2, 368, 335)
    c.line(368, 335, 269, 335)
    c.line(269, 335, 269, 320)
    c.setFillColor(RED)
    c.circle(269, 320, 3, stroke=0, fill=1)

    text(c, "WHAT IS PRESET AND WHAT IS DYNAMIC", 36, 225, 500, 10, NAVY, True)
    card(c, 36, 82, 360, 125, "PRESET FOR THE PROTOTYPE", "Simple release rule; permitted data and disclosure boundaries; recipient and release contract; controlled German/English test requests; stop reasons; receipt schema.", WHITE, BLUE)
    card(c, 414, 82, 392, 125, "DYNAMIC FOR EACH ATTEMPT", "Free request; exact agent decision; permitted relevant context; one new FactHarbor analysis; supporting and opposing evidence; limitations and uncertainty; release or stop outcome.", WHITE, TEAL)

    text(c, "BOUNDARY", 36, 62, 80, 7.5, ORANGE, True)
    text(c, "The prototype releases a checked decision. It does not execute or authorize a resulting action. Controlled tests avoid multiple independent decision and effect paths.", 112, 62, 694, 7.4, INK, False, 9)


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

    text(c, "PROTOTYPE NOW", 36, 218, 250, 10, NAVY, True)
    text(c, "LATER PRODUCT WORK", 430, 218, 300, 10, NAVY, True)
    card(c, 36, 84, 350, 115, "ONE CONTROLLED DECISION RELEASE", "Free request; one exact decision; dynamic FactHarbor examination; simple release-or-stop rule; exact Commit binding; receipt for release and stop. Resulting actions remain outside scope.", WHITE, BLUE)
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
            "/Subject": "Dynamic decision examination in the selected prototype and later effect authorization",
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
