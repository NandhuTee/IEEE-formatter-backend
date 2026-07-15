"""
===============================================================================
Document Analyzer
===============================================================================

80% Rule-based
20% Ollama
"""

from formatter.ollama_client import analyze_with_ollama
from formatter.parser import parse_ai_response


def analyze_document(data):

    result = data.copy()

    need_ai = False

    # Check whether important fields are missing
    if not result["title"]:
        need_ai = True

    if len(result["authors"]) == 0:
        need_ai = True

    if not result["abstract"]:
        need_ai = True

    if len(result["keywords"]) == 0:
        need_ai = True

    if need_ai:

        print("Using Ollama for missing information...")

        text = "\n".join(
            p["text"] for p in result["paragraphs"]
        )

        ai_response = analyze_with_ollama(text)

        ai = parse_ai_response(ai_response)

        if not result["title"]:
            result["title"] = ai["title"]

        if not result["authors"]:
            result["authors"] = ai["authors"]

        if not result["affiliations"]:
            result["affiliations"] = ai["affiliations"]

        if not result["abstract"]:
            result["abstract"] = ai["abstract"]

        if not result["keywords"]:
            result["keywords"] = ai["keywords"]

    return result