from docx import Document

from formatter.reference_extractor import extract_references

doc = Document("uploads/harmonics modified 07.04.26.docx")

references = extract_references(doc)

print()

print("Reference Count :", len(references))

print()

for ref in references:

    print(ref)