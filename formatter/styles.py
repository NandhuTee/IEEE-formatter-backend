from docx.shared import Pt

def set_body_font(run):
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)

def set_title_font(run):
    run.font.name = "Times New Roman"
    run.font.size = Pt(24)
    run.bold = True

def set_heading_font(run):
    run.font.name = "Times New Roman"
    run.font.size = Pt(10)
    run.bold = True