from formatter.extractor import extract_document
from formatter.analyzer import analyze_document

doc = extract_document(
    "uploads/harmonics modified 07.04.26.docx"
)

analysis = analyze_document(doc)

print()

for key, value in analysis.items():

    print("==========", key, "==========")

    print(value)

    print()