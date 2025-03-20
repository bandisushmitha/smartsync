import pdfplumber
import re
import nltk
from nltk.tokenize import word_tokenize

nltk.download("punkt")

def parse_resume(pdf_file):
    with pdfplumber.open(pdf_file) as pdf:
        text = " ".join(page.extract_text() for page in pdf.pages if page.extract_text())

    words = word_tokenize(text.lower())

    skills = [word for word in words if word in {"python", "java", "machine learning", "nlp", "deep learning"}]
    experience = len(re.findall(r"\b[0-9]{1,2}\s*years\b", text))

    return {"Name": pdf_file.name, "Skills": ", ".join(set(skills)), "Experience": experience}
