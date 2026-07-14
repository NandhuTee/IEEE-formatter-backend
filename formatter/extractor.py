from docx import Document
from formatter.models import DocumentModel

COMMON_HEADINGS = {
    "abstract",
    "keywords",
    "introduction",
    "related work",
    "methodology",
    "methods",
    "results",
    "discussion",
    "conclusion",
    "references"
}


def extract_document(file_path):
    doc = Document(file_path)

    model = DocumentModel()

    paragraphs = []

    # -------------------------
    # Read paragraphs
    # -------------------------
    for para in doc.paragraphs:
        text = para.text.strip()

        if not text:
            continue

        paragraphs.append(text)

    # -------------------------
    # Basic information
    # -------------------------
    if len(paragraphs) > 0:
        model.title = paragraphs[0]

    if len(paragraphs) > 1:
        model.authors = [paragraphs[1]]

    # -------------------------
    # Affiliations
    # -------------------------
    i = 2

    while i < len(paragraphs):
        text = paragraphs[i]

        if text.lower().startswith("abstract"):
            break

        model.affiliations.append(text)
        i += 1

    # -------------------------
    # Abstract
    # -------------------------
    if i < len(paragraphs):
        model.abstract = paragraphs[i]

    # -------------------------
    # Detect headings
    # -------------------------
    for para in doc.paragraphs:

        text = para.text.strip()

        if not text:
            continue

        style_name = para.style.name.lower()

        if style_name.startswith("heading") or text.lower() in COMMON_HEADINGS:
            model.sections.append({
                "title": text,
                "level": 1
            })

    # -------------------------
    # Extract tables
    # -------------------------
    for index, table in enumerate(doc.tables, start=1):

        rows = []

        for row in table.rows:
            rows.append([cell.text.strip() for cell in row.cells])

        model.tables.append({
            "id": index,
            "caption": "",
            "rows": rows
        })

    # -------------------------
    # Placeholder for figures
    # -------------------------
    model.figures = []

    # -------------------------
    # Placeholder for references
    # -------------------------
    model.references = []

    return model