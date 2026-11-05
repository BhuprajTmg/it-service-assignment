#!/usr/bin/env python3
"""Generate a tailored CV .docx for Bhupraj Tamang - Customer Service Advisor (Sportsbet, Darwin)."""
from docx import Document
from docx.shared import Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY = RGBColor(0x17, 0x2A, 0x42)
GREY = RGBColor(0x5A, 0x5A, 0x5A)
BLACK = RGBColor(0x14, 0x14, 0x14)

doc = Document()

section = doc.sections[0]
section.top_margin = Mm(14)
section.bottom_margin = Mm(14)
section.left_margin = Mm(16)
section.right_margin = Mm(16)

style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(10)
style.paragraph_format.space_after = Pt(0)
style.paragraph_format.space_before = Pt(0)


def add_rule(paragraph, color="172A42", size=8):
    pPr = paragraph._p.get_or_add_pPr()
    pBdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    pBdr.append(bottom)
    pPr.append(pBdr)


def section_title(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run(text.upper())
    run.bold = True
    run.font.size = Pt(12)
    run.font.color.rgb = NAVY
    add_rule(p)
    return p


def job_header(title, company_dates):
    p1 = doc.add_paragraph()
    p1.paragraph_format.space_after = Pt(0)
    r1 = p1.add_run(title)
    r1.bold = True
    r1.font.size = Pt(10.5)
    r1.font.color.rgb = BLACK

    p2 = doc.add_paragraph()
    p2.paragraph_format.space_after = Pt(3)
    r2 = p2.add_run(company_dates)
    r2.italic = True
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = GREY


def bullet(text):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.font.size = Pt(9.8)
    r.font.color.rgb = BLACK


def body_text(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(4)
    r = p.add_run(text)
    r.font.size = Pt(9.8)
    r.font.color.rgb = BLACK


# Name & title
p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(1)
r = p.add_run("BHUPRAJ TAMANG")
r.bold = True
r.font.size = Pt(22)
r.font.color.rgb = NAVY

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
r = p.add_run("Customer Service Advisor")
r.bold = True
r.font.size = Pt(12)
r.font.color.rgb = GREY

p = doc.add_paragraph()
p.paragraph_format.space_after = Pt(2)
r = p.add_run("Darwin, NT, Australia  |  bhupraj875@email.com  |  +61 447 481 904  |  LinkedIn  |  Portfolio")
r.font.size = Pt(9.5)
r.font.color.rgb = BLACK
add_rule(p, size=16)

# Professional Summary
section_title("Professional Summary")
body_text(
    "Friendly, reliable customer service professional who enjoys helping people and solving "
    "problems with a smile. Comfortable working to targets in a fast-paced team environment, "
    "with strong communication skills and a calm approach under pressure. Based in Darwin and "
    "currently studying a Master of IT at Charles Darwin University. I genuinely enjoy "
    "customer-facing work and would feel great being part of a fun, high-energy team like "
    "Sportsbet's."
)

# Key Strengths
section_title("Key Strengths")
for s in [
    "Friendly, confident communicator, in person and on the phone",
    "Calm and clear-headed under pressure",
    "Strong attention to detail",
    "Reliable, punctual and target-driven",
    "Good computer skills (Outlook, Excel, web-based systems)",
    "Team player who enjoys helping others",
    "Flexible with rotating shifts, including evenings and weekends",
]:
    bullet(s)

# Relevant Experience
section_title("Relevant Experience")

job_header("Customer Service Team Member", "Coles Supermarkets | Darwin, NT | [Add dates]")
for b in [
    "Greeted and helped customers every day, answering questions and solving problems quickly.",
    "Handled payments, enquiries and complaints at the checkout and service desk with a "
    "positive attitude.",
    "Communicated clearly with customers and teammates to keep things running smoothly.",
    "Stayed calm, friendly and efficient during busy, high-pressure periods.",
]:
    bullet(b)

# Education
section_title("Education")
job_header("Master of Information Technology (Information Systems)",
           "Charles Darwin University, Casuarina, NT | Expected November 2027 (Currently Enrolled)")
job_header("Bachelor of Science (Honours) in Computing",
           "Softwarica College of IT & E-Commerce (Coventry University) | Graduated September 2023")

# Availability
section_title("Availability")
body_text(
    "Based in Darwin, NT. Available for the 3 weeks of full-time training from 8 December 2026 "
    "(including Saturdays) and happy to work rotating shifts, including evenings and weekends."
)

doc.save("CV_Bhupraj_Tamang_Customer_Service_Advisor.docx")
print("done")
