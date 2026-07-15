"""
===============================================================================
IEEE RULE ENGINE
===============================================================================

Purpose
-------
This module contains ONLY IEEE formatting rules.

Responsibilities
----------------
✔ Page Layout
✔ Fonts
✔ Font Sizes
✔ Alignment
✔ Paragraph Formatting
✔ Table Formatting
✔ Figure Caption Formatting
✔ Reference Formatting

This module DOES NOT:
---------------------
❌ Read DOCX files
❌ Extract text
❌ Call Ollama
❌ Perform AI analysis
❌ Validate documents

Every formatting function receives an existing Paragraph/Table object
and applies IEEE formatting.

===============================================================================
"""

from docx.shared import Pt, Mm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT


# =============================================================================
# PAGE LAYOUT
# =============================================================================

def apply_page_layout(doc):
    """
    Configure IEEE page settings.

    IEEE Conference Paper

    Paper Size : A4
    Top Margin : 19 mm
    Bottom     : 25.4 mm
    Left       : 16.5 mm
    Right      : 16.5 mm
    """

    section = doc.sections[0]

    section.page_width = Mm(210)
    section.page_height = Mm(297)

    section.top_margin = Mm(19)
    section.bottom_margin = Mm(25.4)

    section.left_margin = Mm(16.5)
    section.right_margin = Mm(16.5)


# =============================================================================
# TITLE
# =============================================================================

def format_title(paragraph):
    """
    IEEE Paper Title

    Font : Times New Roman
    Size : 24 pt
    Style: Bold
    Align: Center
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(24)
        run.bold = True


# =============================================================================
# AUTHORS
# =============================================================================

def format_authors(paragraph):
    """
    Author Names

    Font : Times New Roman
    Size : 11 pt
    Align: Center
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(11)


# =============================================================================
# AFFILIATIONS
# =============================================================================

def format_affiliations(paragraph):
    """
    Author Affiliations

    Font : Times New Roman
    Size : 10 pt
    Align: Center
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)


# =============================================================================
# ABSTRACT HEADING
# =============================================================================

def format_abstract_heading(paragraph):
    """
    Abstract Heading

    Font : Times New Roman
    Size : 10 pt
    Style: Bold
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.bold = True


# =============================================================================
# ABSTRACT TEXT
# =============================================================================

def format_abstract(paragraph):
    """
    Abstract Content

    Font : Times New Roman
    Size : 10 pt
    Align: Justify
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)


# =============================================================================
# KEYWORDS
# =============================================================================

def format_keywords(paragraph):
    """
    Keywords

    Font : Times New Roman
    Size : 10 pt
    Style: Italic
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.italic = True


# =============================================================================
# LEVEL 1 HEADING
# =============================================================================

def format_heading1(paragraph):
    """
    IEEE Level 1 Heading

    Font : Times New Roman
    Size : 10 pt
    Style: Bold
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.bold = True


# =============================================================================
# LEVEL 2 HEADING
# =============================================================================

def format_heading2(paragraph):
    """
    IEEE Level 2 Heading

    Font : Times New Roman
    Size : 10 pt
    Style: Bold Italic
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.bold = True
        run.italic = True


# =============================================================================
# LEVEL 3 HEADING
# =============================================================================

def format_heading3(paragraph):
    """
    IEEE Level 3 Heading

    Font : Times New Roman
    Size : 10 pt
    Style: Italic
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.italic = True


# =============================================================================
# BODY PARAGRAPH
# =============================================================================

def format_body(paragraph):
    """
    Main Body Text

    Font : Times New Roman
    Size : 10 pt
    Align: Justify
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)


# =============================================================================
# TABLE CAPTION
# =============================================================================

def format_table_caption(paragraph):
    """
    Table Caption

    Example:
    TABLE I
    COMPARISON OF METHODS
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(9)
        run.bold = True


# =============================================================================
# FIGURE CAPTION
# =============================================================================

def format_figure_caption(paragraph):
    """
    Figure Caption

    Example:
    Fig. 1. System Architecture
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)


# =============================================================================
# TABLE
# =============================================================================

def format_table(table):
    """
    Apply IEEE table formatting.

    - Center table
    - Font 9 pt
    """

    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.name = "Times New Roman"
                    run.font.size = Pt(9)


# =============================================================================
# REFERENCES HEADING
# =============================================================================

def format_reference_heading(paragraph):
    """
    References Heading
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)
        run.bold = True


# =============================================================================
# REFERENCE ENTRY
# =============================================================================

def format_reference(paragraph):
    """
    Individual Reference

    Font : Times New Roman
    Size : 8 pt
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(8)


# =============================================================================
# EQUATIONS (Placeholder)
# =============================================================================

def format_equation(paragraph):
    """
    Reserved for future equation formatting.
    """

    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER

    for run in paragraph.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(10)