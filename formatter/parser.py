def parse_ai_response(text):

    result = {
        "title": "",
        "authors": [],
        "affiliations": [],
        "abstract": "",
        "keywords": [],
        "sections": [],
        "references": []
    }

    current = None

    for line in text.splitlines():

        line = line.strip()

        if not line:
            continue

        upper = line.upper()

        if upper == "TITLE:":
            current = "title"
            continue

        elif upper == "AUTHORS:":
            current = "authors"
            continue

        elif upper == "AFFILIATIONS:":
            current = "affiliations"
            continue

        elif upper == "ABSTRACT:":
            current = "abstract"
            continue

        elif upper == "KEYWORDS:":
            current = "keywords"
            continue

        elif upper == "SECTIONS:":
            current = "sections"
            continue

        elif upper == "REFERENCES:":
            current = "references"
            continue

        if current == "title":
            result["title"] = line

        elif current == "abstract":
            result["abstract"] += line + " "

        else:
            result[current].append(line)

    return result