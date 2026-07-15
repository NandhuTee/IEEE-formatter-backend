from formatter.extractor import extract_document
from formatter.analyzer import analyze_document
from formatter.ieee_formatter import create_ieee_document

# Input document
input_file = "uploads/harmonics modified 07.04.26.docx"

# Output document
output_file = "output/IEEE_Output.docx"

# Step 1: Extract
data = extract_document(input_file)

# Step 2: Analyze
analysis = analyze_document(data)

# Step 3: Generate IEEE document
create_ieee_document(
    analysis,
    output_file
)

print("IEEE document created successfully!")
print("Output:", output_file)