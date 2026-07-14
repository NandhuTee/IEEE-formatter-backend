from docx import Document
from docx.shared import Pt
from docx.enum.section import WD_SECTION
from docx.shared import Mm
from docx.shared import Pt

def set_ieee_page_layout(doc):
    section = doc.sections[0]

    # A4 size
    section.page_width = Mm(210)
    section.page_height = Mm(297)

    # IEEE margins (adjust later if needed)
    section.top_margin = Mm(19)
    section.bottom_margin = Mm(25)
    section.left_margin = Mm(16)
    section.right_margin = Mm(16)


def add_title(doc, text):
    p = doc.add_paragraph()

    run = p.add_run(text)

    run.font.name = "Times New Roman"
    run.font.size = Pt(24)
    run.bold = True

    p.alignment = 1

#Authors
def add_authors(doc, text):
    p = doc.add_paragraph()

    run = p.add_run(text)

    run.font.name = "Times New Roman"
    run.font.size = Pt(11)

    p.alignment = 1

def add_affiliation(doc, text):
    p = doc.add_paragraph()

    run = p.add_run(text)

    run.font.name = "Times New Roman"
    run.font.size = Pt(10)

    p.alignment = 1

def add_abstract(doc, text):

    h = doc.add_heading("Abstract", level=1)

    h.runs[0].font.name = "Times New Roman"

    p = doc.add_paragraph()

    run = p.add_run(text)

    run.font.name = "Times New Roman"
    run.font.size = Pt(10)

def create_ieee_document(data, output_file):

    doc = Document()

    set_ieee_page_layout(doc)

    add_title(doc, data["title"])

    add_authors(doc, data["authors"])

    for aff in data["affiliations"]:
        add_affiliation(doc, aff)

    add_abstract(doc, data["abstract"])

    set_ieee_page_layout(doc)
    # Title
    title = doc.add_heading(data["title"], level=0)
    title.runs[0].font.name = "Times New Roman"
    title.runs[0].font.size = Pt(24)

    # Authors
    p = doc.add_paragraph()
    run = p.add_run(data["authors"])
    run.font.name = "Times New Roman"
    run.font.size = Pt(11)

    # Affiliations
    for aff in data["affiliations"]:
        p = doc.add_paragraph()
        run = p.add_run(aff)
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)

    # Abstract
    h = doc.add_heading("Abstract", level=1)
    h.runs[0].font.name = "Times New Roman"

    p = doc.add_paragraph(data["abstract"])

    # Body
    for para in data["body"]:
        doc.add_paragraph(para)

    # References
    if data["references"]:
        doc.add_heading("References", level=1)

        for ref in data["references"]:
            doc.add_paragraph(ref)

    doc.save(output_file)

    