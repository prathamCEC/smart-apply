
import pymupdf
import re
from pathlib import Path


def extract_resume_text(pdf_path):
    """
    Extract and clean text from a PDF resume.
    """

    pdf_path = Path(pdf_path)

    if not pdf_path.exists():
        raise FileNotFoundError("Resume PDF not found.")

    if pdf_path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are supported.")

    extracted_text = []

    with pymupdf.open(pdf_path) as document:

        if document.is_encrypted:
            raise ValueError("Encrypted PDFs are not supported.")

        for page in document:
            page_text = page.get_text("text")
            extracted_text.append(page_text)

    text = "\n".join(extracted_text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    if not text:
        raise ValueError(
            "No readable text found. The PDF may be scanned."
        )

    return text
