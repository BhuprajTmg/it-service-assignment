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
summary = ("Friendly, reliable customer service professional who enjoys helping people and solving "
           "problems with a smile. Comfortable working to targets in a fast-paced team environment, "
           "with strong communication skills and a calm approach under pressure. Based in Darwin and "
           "currently studying a Master of IT at Charles Darwin University. I genuinely enjoy "
           "customer-facing work and would feel great being part of a fun, high-energy team like "
           "Sportsbet's.")
pdf.body_text(summary)

# Key Strengths / Skills tailored to job
pdf.section_title("Key Strengths")
strengths = [
    "Friendly, confident communicator, in person and on the phone",
    "Calm and clear-headed under pressure",
    "Strong attention to detail",
    "Reliable, punctual and target-driven",
    "Good computer skills (Outlook, Excel, web-based systems)",
    "Team player who enjoys helping others",
    "Flexible with rotating shifts, including evenings and weekends",
]
for s in strengths:
    pdf.bullet(s)

# Relevant Experience
pdf.section_title("Relevant Experience")

pdf.job_header("Customer Service Team Member", "Coles Supermarkets | Darwin, NT | [Add dates]")
for b in [
    "Greeted and helped customers every day, answering questions and solving problems quickly.",
    "Handled payments, enquiries and complaints at the checkout and service desk with a "
    "positive attitude.",
    "Communicated clearly with customers and teammates to keep things running smoothly.",
    "Stayed calm, friendly and efficient during busy, high-pressure periods.",
]:
    pdf.bullet(b)

# Education
pdf.section_title("Education")
pdf.job_header("Master of Information Technology (Information Systems)",
               "Charles Darwin University, Casuarina, NT | Expected November 2027 (Currently Enrolled)")
pdf.ln(1)
pdf.job_header("Bachelor of Science (Honours) in Computing",
               "Softwarica College of IT & E-Commerce (Coventry University) | Graduated September 2023")

# Availability / fit note
pdf.section_title("Availability")
pdf.body_text(
    "Based in Darwin, NT. Available for the 3 weeks of full-time training from 8 December 2026 "
    "(including Saturdays) and happy to work rotating shifts, including evenings and weekends."
)

pdf.output("CV_Bhupraj_Tamang_Customer_Service_Advisor.pdf")
print("done")
