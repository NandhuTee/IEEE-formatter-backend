from fastapi import FastAPI, UploadFile, File
import os
import shutil

from formatter.extractor import extract_document
from formatter.analyzer import analyze_document
from formatter.ieee_formatter import create_ieee_document

app = FastAPI(title="IEEE Formatter API")

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "IEEE Formatter Backend Running"
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract document
    result = extract_document(file_path)

    # Analyze document
    analysis = analyze_document(result)

    # Create IEEE document
    output_path = os.path.join(OUTPUT_FOLDER, "IEEE_Output.docx")

    create_ieee_document(
        analysis,
        output_path
    )

    # Return response
    return {
        "message": "IEEE document created successfully",
        "output_file": output_path
    }