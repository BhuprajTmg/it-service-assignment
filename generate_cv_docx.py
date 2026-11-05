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
    "Reliable and detail-focused professional with proven experience delivering 24/7 support "
    "in fast-paced, high-pressure environments. Skilled at resolving issues clearly and "
    "calmly under time pressure, keeping accurate records, and working closely with "
    "cross-functional teams to get problems solved quickly. Strong computer literacy across "
    "reporting, data and office systems, with a track record of meeting performance targets "
    "and maintaining quality and compliance standards. Based in Darwin and currently studying "
    "a Master of IT at Charles Darwin University, bringing a calm, team-first attitude, "
    "flexibility for rotating rosters, and a genuine enjoyment of helping people."
)

# Key Strengths
section_title("Key Strengths")
for s in [
    "Clear, confident communication - built through daily phone, email and stakeholder "
    "communication while providing 24/7 on-call technical support",
    "Calm under pressure - resolved critical, time-sensitive issues to minimise downtime, "
    "staying composed and solution-focused throughout",
    "Attention to detail & accuracy - meticulous record-keeping, documentation and data "
    "handling across every role",
    "Working to KPIs & quality standards - consistently met performance, reliability and "
    "compliance benchmarks in regulated, structured environments",
    "Strong computer skills - highly proficient with Microsoft Outlook, Excel and multiple "
    "web-based/enterprise systems (SQL tools, dashboards, ticketing & monitoring platforms)",
    "Team-first collaborator - worked closely with cross-functional teams (support, "
    "engineering, stakeholders) to resolve issues quickly and share knowledge",
    "Adaptable & quick learner - picked up new tools, platforms and processes rapidly "
    "across multiple employers and technical domains",
    "Flexible availability - comfortable working rotating shifts, including evenings and "
    "weekends, to support round-the-clock operations",
]:
    bullet(s)

# Relevant Experience
section_title("Relevant Experience")

job_header("Associate Database Administrator",
           "Cedar Gate Services Pvt. Ltd. | Kathmandu, Nepal | Jan 2025 - Nov 2026")
for b in [
    "Provided 24/7 on-call support, communicating clearly with stakeholders to resolve "
    "critical issues promptly and keep disruption to a minimum - directly comparable to "
    "handling urgent customer enquiries under time pressure.",
    "Kept detailed, accurate records of issues, actions and resolutions to support "
    "consistency, accountability and continuous improvement.",
    "Automated routine processes to improve reliability and free up time for higher-value, "
    "people-facing problem solving.",
    "Monitored performance against targets daily, proactively flagging and resolving issues "
    "before they escalated.",
]:
    bullet(b)

job_header("Database Administrator (Trainee)",
           "Dish Media Network Ltd. | Kathmandu, Nepal | Sept 2023 - Dec 2024")
for b in [
    "Managed complex, sensitive data migrations with zero tolerance for error, ensuring "
    "accuracy and integrity throughout - reflecting strong attention to detail and "
    "reliability under pressure.",
    "Liaised with internal teams to troubleshoot and resolve technical problems quickly, "
    "building skills in clear communication and collaborative problem-solving.",
    "Built interactive dashboards to turn complex information into clear, easy-to-understand "
    "insights for non-technical stakeholders - a strength directly transferable to explaining "
    "betting products, promotions and account information to customers.",
    "Maintained thorough documentation to support compliance and quality standards.",
]:
    bullet(b)

# Education
section_title("Education")
job_header("Master of Information Technology (Information Systems)",
           "Charles Darwin University, Casuarina, NT | Expected November 2027 (Currently Enrolled)")
job_header("Bachelor of Science (Honours) in Computing",
           "Softwarica College of IT & E-Commerce (Coventry University) | Graduated September 2023")

# Certifications & Membership
section_title("Certifications & Membership")
for c in [
    "Oracle Cloud Infrastructure 2025 Certified Foundations Associate",
    "Data Analytics for Business with Tableau Training",
    "Administration of Red Hat Linux Systems",
    "Oracle SQL Track",
    "Associate Member of the Australian Computer Society (ACS)",
]:
    bullet(c)

# Availability
section_title("Availability")
body_text(
    "Based in Darwin, NT. Available to commit to 3 weeks of full-time training from "
    "8 December 2026 (including Saturdays) and flexible for rotating rosters, including "
    "evenings, weekends and public holidays."
)

doc.save("CV_Bhupraj_Tamang_Customer_Service_Advisor.docx")
print("done")
