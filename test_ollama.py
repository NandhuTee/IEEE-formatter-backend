from formatter.ollama_client import analyze_with_ollama

text = """
Physics-Informed Machine Learning-Based Adaptive Harmonic Mitigation

Sudha K

Abstract

This paper proposes...
"""

result = analyze_with_ollama(text)

print(result)