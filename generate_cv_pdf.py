#!/usr/bin/env python3
"""Generate a tailored CV PDF for Bhupraj Tamang - Customer Service Advisor (Sportsbet, Darwin)."""
from fpdf import FPDF

NAVY = (23, 42, 66)
GREY = (90, 90, 90)
BLACK = (20, 20, 20)
LINE = (210, 214, 220)

class CV(FPDF):
    def header(self):
        pass

    def footer(self):
        pass

    def section_title(self, title):
        self.ln(3)
        self.set_font("Helvetica", "B", 12)
        self.set_text_color(*NAVY)
        self.cell(0, 7, title.upper(), new_x="LMARGIN", new_y="NEXT")
        y = self.get_y()
        self.set_draw_color(*NAVY)
        self.set_line_width(0.5)
        self.line(self.l_margin, y, self.w - self.r_margin, y)
        self.ln(2)
        self.set_text_color(*BLACK)

    def job_header(self, title, company_dates):
        self.set_font("Helvetica", "B", 10.5)
        self.set_text_color(*BLACK)
        self.cell(0, 5.5, title, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Helvetica", "I", 9.5)
        self.set_text_color(*GREY)
        self.cell(0, 5, company_dates, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*BLACK)

    def bullet(self, text):
        self.set_font("Helvetica", "", 9.8)
        self.set_x(self.l_margin + 4)
        self.multi_cell(self.w - self.l_margin - self.r_margin - 4, 5, f"-  {text}")

    def body_text(self, text, size=9.8, style=""):
        self.set_font("Helvetica", style, size)
        self.multi_cell(0, 5, text)


pdf = CV(format="A4", unit="mm")
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_left_margin(16)
pdf.set_right_margin(16)
pdf.set_top_margin(14)

# Name
pdf.set_font("Helvetica", "B", 22)
pdf.set_text_color(*NAVY)
pdf.cell(0, 10, "BHUPRAJ TAMANG", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("Helvetica", "B", 12)
pdf.set_text_color(*GREY)
pdf.cell(0, 6.5, "Customer Service Advisor", new_x="LMARGIN", new_y="NEXT")

pdf.set_font("Helvetica", "", 9.5)
pdf.set_text_color(*BLACK)
pdf.cell(0, 5.5, "Darwin, NT, Australia  |  bhupraj875@email.com  |  +61 447 481 904  |  LinkedIn  |  Portfolio",
         new_x="LMARGIN", new_y="NEXT")

pdf.ln(1)
pdf.set_draw_color(*NAVY)
pdf.set_line_width(0.8)
pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())

# Professional Summary
pdf.section_title("Professional Summary")
summary = ("Reliable and detail-focused professional with proven experience delivering 24/7 support "
           "in fast-paced, high-pressure environments. Skilled at resolving issues clearly and "
           "calmly under time pressure, keeping accurate records, and working closely with "
           "cross-functional teams to get problems solved quickly. Strong computer literacy across "
           "reporting, data and office systems, with a track record of meeting performance targets "
           "and maintaining quality and compliance standards. Based in Darwin and currently studying "
           "a Master of IT at Charles Darwin University, bringing a calm, team-first attitude, "
           "flexibility for rotating rosters, and a genuine enjoyment of helping people.")
pdf.body_text(summary)

# Key Strengths / Skills tailored to job
pdf.section_title("Key Strengths")
strengths = [
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
]
for s in strengths:
    pdf.bullet(s)

# Relevant Experience (reframed)
pdf.section_title("Relevant Experience")

pdf.job_header("Associate Database Administrator", "Cedar Gate Services Pvt. Ltd. | Kathmandu, Nepal | Jan 2025 - Nov 2026")
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
    pdf.bullet(b)
pdf.ln(1)

pdf.job_header("Database Administrator (Trainee)", "Dish Media Network Ltd. | Kathmandu, Nepal | Sept 2023 - Dec 2024")
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
    pdf.bullet(b)

# Education
pdf.section_title("Education")
pdf.job_header("Master of Information Technology (Information Systems)",
               "Charles Darwin University, Casuarina, NT | Expected November 2027 (Currently Enrolled)")
pdf.ln(1)
pdf.job_header("Bachelor of Science (Honours) in Computing",
               "Softwarica College of IT & E-Commerce (Coventry University) | Graduated September 2023")

# Certifications & Membership
pdf.section_title("Certifications & Membership")
for c in [
    "Oracle Cloud Infrastructure 2025 Certified Foundations Associate",
    "Data Analytics for Business with Tableau Training",
    "Administration of Red Hat Linux Systems",
    "Oracle SQL Track",
    "Associate Member of the Australian Computer Society (ACS)",
]:
    pdf.bullet(c)

# Availability / fit note
pdf.section_title("Availability")
pdf.body_text(
    "Based in Darwin, NT. Available to commit to 3 weeks of full-time training from "
    "8 December 2026 (including Saturdays) and flexible for rotating rosters, including "
    "evenings, weekends and public holidays."
)

pdf.output("CV_Bhupraj_Tamang_Customer_Service_Advisor.pdf")
print("done")
