"""
===============================================================================
Table Extractor
===============================================================================

Purpose
-------
Extract every table from the uploaded DOCX document.

Responsibilities
----------------
✔ Preserve table order
✔ Preserve rows
✔ Preserve columns
✔ Preserve cell values

Future Enhancements
-------------------
□ Detect merged cells
□ Detect table captions
□ Preserve table styles
□ Preserve borders

===============================================================================
"""

from docx import Document


def extract_tables(doc: Document):

    tables = []

    for table_index, table in enumerate(doc.tables, start=1):

        table_data = {
            "id": table_index,
            "caption": "",
            "rows": [],
            "row_count": len(table.rows),
            "column_count": len(table.columns)
        }

        for row in table.rows:

            row_data = []

            for cell in row.cells:

                row_data.append(cell.text.strip())

            table_data["rows"].append(row_data)

        tables.append(table_data)

    return tables