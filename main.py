from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
import shutil
from fastapi.middleware.cors import CORSMiddleware
from formatter.extractor import extract_document
from formatter.analyzer import analyze_document
from formatter.ieee_formatter import create_ieee_document
from formatter.validator import validate_document
from formatter.ollama_client import analyze_with_ollama
from models import GenerateRequest

app = FastAPI(title="IEEE Formatter API")

# ==========================
# CORS Configuration
# ==========================

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

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

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted = extract_document(file_path)

    analysis = analyze_document(extracted)

    errors = validate_document(analysis)

    return {
        "status": "success",
        "document": analysis,
        "errors": errors
    }

@app.get("/download/{filename}")
def download_file(filename: str):

    file_path = os.path.join(OUTPUT_FOLDER, filename)

    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404,
            detail="File not found"
        )

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

@app.post("/generate")
def generate_document(data: GenerateRequest):

    output_file = os.path.join(
        OUTPUT_FOLDER,
        "IEEE_Output.docx"
    )

    create_ieee_document(
        data.model_dump(),
        output_file
    )

    return {
        "status": "success",
        "download_url": "/download/IEEE_Output.docx"
    }