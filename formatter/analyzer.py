def analyze_document(data):
    result = {
        "title": data.title,
        "authors": data.get("authors", ""),
        "affiliations": data.get("affiliations", []),
        "abstract": "",
        "keywords": "",
        "body": [],
        "references": []
    }

    paragraphs = data.get("paragraphs", [])

    in_abstract = False
    in_references = False

    for p in paragraphs:

        text = p.strip()

        if text.lower().startswith("abstract"):
            in_abstract = True
            result["abstract"] = text
            continue

        if text.lower().startswith("keywords"):
            result["keywords"] = text
            in_abstract = False
            continue

        if text.lower().startswith("references"):
            in_references = True
            continue

        if in_references:
            result["references"].append(text)
        else:
            result["body"].append(text)

    return result