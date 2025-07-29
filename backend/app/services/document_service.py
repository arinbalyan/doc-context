import requests
from pypdf import PdfReader
from docx import Document
import io

def process_document(url: str) -> str:
    response = requests.get(url)
    response.raise_for_status()

    content_type = response.headers.get('Content-Type', '').lower()
    text = ""

    if "application/pdf" in content_type or url.endswith(".pdf"):
        pdf_reader = PdfReader(io.BytesIO(response.content))
        text = "".join(page.extract_text() for page in pdf_reader.pages)
    elif "application/vnd.openxmlformats-officedocument.wordprocessingml.document" in content_type or url.endswith(".docx"):
        doc = Document(io.BytesIO(response.content))
        text = "\n".join(para.text for para in doc.paragraphs)
    else:
        # Treat as general text content, which includes emails, HTML, plain text, etc.
        text = response.text

    return text
