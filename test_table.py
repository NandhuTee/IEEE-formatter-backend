from docx import Document
from formatter.table_extractor import extract_tables

doc = Document("uploads/harmonics modified 07.04.26.docx")

tables = extract_tables(doc)

print(tables)