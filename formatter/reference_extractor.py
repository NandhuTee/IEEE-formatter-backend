"""
===============================================================================
Reference Extractor
===============================================================================

Purpose
-------
Extract all references from a DOCX document.

Responsibilities
----------------
✔ Detect References heading
✔ Extract all reference entries
✔ Preserve order

Future
------
□ DOI extraction
□ IEEE reference validation
□ CrossRef integration

===============================================================================
"""


def extract_references(doc):

    references = []

    in_references = False

    for para in doc.paragraphs:

        text = para.text.strip()

        if not text:
            continue

        lower = text.lower()

        # Detect References section
        if lower == "references":

            in_references = True

            continue

        if in_references:

            references.append(text)

    return references