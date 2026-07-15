"""
===============================================================================
Main Extractor
===============================================================================
"""

from docx import Document

from formatter.paragraph_extractor import extract_paragraphs
from formatter.heading_extractor import extract_headings
from formatter.table_extractor import extract_tables
from formatter.image_extractor import extract_images
from formatter.reference_extractor import extract_references



def extract_document(file_path):

    doc = Document(file_path)

    # Extract document parts
    paragraphs = extract_paragraphs(doc)
    headings = extract_headings(doc)
    tables = extract_tables(doc)
    figures = extract_images(doc)
    references = extract_references(doc)
   

    # Convert paragraph objects to plain text
    paragraph_text = [p["text"] for p in paragraphs]

    # ---------------------------------------------------------
    # Rule-based extraction (80%)
    # ---------------------------------------------------------

    title = ""
    authors = []
    affiliations = []
    abstract = ""
    keywords = []

    if len(paragraph_text) > 0:
        title = paragraph_text[0]

    if len(paragraph_text) > 1:
        authors.append(paragraph_text[1])

    # Affiliations
    i = 2

    while i < len(paragraph_text):

        text = paragraph_text[i]

        if text.lower().startswith("abstract"):
            break

        affiliations.append(text)

        i += 1

    # Abstract
    if i < len(paragraph_text):

        abstract = paragraph_text[i]

    # Keywords
    for text in paragraph_text:

        if text.lower().startswith("keywords"):

            keyword_text = text.replace("Keywords", "")
            keyword_text = keyword_text.replace(":", "")

            keywords = [
                k.strip()
                for k in keyword_text.split(",")
                if k.strip()
            ]

            break

    return {

        "title": title,

        "authors": authors,

        "affiliations": affiliations,

        "abstract": abstract,

        "keywords": keywords,

        "paragraphs": paragraphs,

        "headings": headings,

        "tables": tables,

        "figures": figures,

        "references": references,

      

    }