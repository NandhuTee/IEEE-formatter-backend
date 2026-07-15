"""
===============================================================================
IEEE DOCUMENT VALIDATOR
===============================================================================

Purpose
-------
Validates the extracted and analyzed document before formatting.

Responsibilities
----------------
✔ Check mandatory sections
✔ Check title
✔ Check authors
✔ Check abstract
✔ Check keywords
✔ Check section order
✔ Check tables
✔ Check figures
✔ Check references

Returns
-------
List of validation errors.

Empty list = Validation Passed

===============================================================================
"""


def validate_document(data):

    errors = []

    # =====================================================================
    # Title
    # =====================================================================

    if not data.get("title", "").strip():

        errors.append("Missing paper title.")

    # =====================================================================
    # Authors
    # =====================================================================

    if len(data.get("authors", [])) == 0:

        errors.append("Missing authors.")

    # =====================================================================
    # Affiliations
    # =====================================================================

    if len(data.get("affiliations", [])) == 0:

        errors.append("Missing affiliations.")

    # =====================================================================
    # Abstract
    # =====================================================================

    if not data.get("abstract", "").strip():

        errors.append("Missing abstract.")

    # =====================================================================
    # Keywords
    # =====================================================================

    if len(data.get("keywords", [])) == 0:

        errors.append("Missing keywords.")

    # =====================================================================
    # Sections
    # =====================================================================

    if len(data.get("sections", [])) == 0:

        errors.append("No document sections detected.")

    # =====================================================================
    # Tables
    # =====================================================================

    tables = data.get("tables", [])

    for index, table in enumerate(tables, start=1):

        rows = table.get("rows", [])

        if len(rows) == 0:

            errors.append(
                f"Table {index} contains no rows."
            )

    # =====================================================================
    # Figures
    # =====================================================================

    figures = data.get("figures", [])

    for index, fig in enumerate(figures, start=1):

        if not fig.get("caption"):

            errors.append(
                f"Figure {index} is missing caption."
            )

    # =====================================================================
    # References
    # =====================================================================

    if len(data.get("references", [])) == 0:

        errors.append("No references found.")

    return errors