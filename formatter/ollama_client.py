"""
Ollama Client

Uses Ollama only for document understanding.

Python Rules = 80%
Ollama = 20%
"""

import os
import json
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL = os.environ.get("OLLAMA_MODEL", "llama3.2:1b")


def analyze_with_ollama(document_text: str):

   PROMPT = f"""
You are an expert academic paper analyzer.

Your job is ONLY to identify the structure.

Do NOT explain.

Do NOT rewrite.

Return EXACTLY in this format.

TITLE:
...

AUTHORS:
...

AFFILIATIONS:
...

ABSTRACT:
...

KEYWORDS:
...

SECTIONS:
...

REFERENCES:
...

Paper:

{document_text}
"""