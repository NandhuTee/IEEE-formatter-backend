"""
===============================================================================
Paragraph Extractor
===============================================================================

Extracts all non-empty paragraphs from a DOCX document while preserving order.
"""

from docx import Document


def extract_paragraphs(doc: Document):

    paragraphs = []

    for index, para in enumerate(doc.paragraphs):

        text = para.text.strip()

        if not text:
            continue

        paragraphs.append({
            "id": index + 1,
            "text": text,
            "style": para.style.name,
            "alignment": para.alignment
        })

    return paragraphs