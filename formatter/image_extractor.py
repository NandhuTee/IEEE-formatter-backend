from docx import Document

from formatter.paragraph_extractor import extract_paragraphs
from formatter.heading_extractor import extract_headings
from formatter.table_extractor import extract_tables
from formatter.reference_extractor import extract_references
import os


def extract_images(doc, output_folder="uploads/images"):

    os.makedirs(output_folder, exist_ok=True)

    images = []

    image_number = 1

    for rel in doc.part.rels.values():

        if "image" not in rel.target_ref:
            continue

        image = rel.target_part.blob

        extension = rel.target_ref.split(".")[-1]

        filename = f"figure_{image_number}.{extension}"

        filepath = os.path.join(output_folder, filename)

        with open(filepath, "wb") as f:
            f.write(image)

        images.append({
            "id": image_number,
            "caption": "",
            "image": filepath
        })

        image_number += 1

    return images