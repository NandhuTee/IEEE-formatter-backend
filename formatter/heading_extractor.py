"""
===============================================================================
Heading Extractor
===============================================================================
"""

COMMON_HEADINGS = {
    "abstract",
    "keywords",
    "introduction",
    "related work",
    "literature review",
    "methodology",
    "methods",
    "results",
    "discussion",
    "conclusion",
    "future work",
    "references"
}


def extract_headings(doc):

    headings = []

    for para in doc.paragraphs:

        text = para.text.strip()

        if not text:
            continue

        style = para.style.name.lower()

        if style.startswith("heading"):

            headings.append({
                "text": text,
                "style": para.style.name
            })

        elif text.lower() in COMMON_HEADINGS:

            headings.append({
                "text": text,
                "style": "Detected"
            })

    return headings