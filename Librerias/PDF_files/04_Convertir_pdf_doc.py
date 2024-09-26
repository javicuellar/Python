import os
from PyPDF2 import PdfReader
#  Instalar librería -> pip install python-docx 
import docx


def pdf_to_text():
    pdf_file = "04_Convertir_pdf_doc.pdf"
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            page_text = reader.pages[page_num].extract_text()
            text += page_text
    return text


def pdf_to_docx(output_file):
    text = pdf_to_text()
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save(output_file)



# Example usage:
output_docx_file = "04_Convertir_pdf_doc.docx"

pdf_to_docx(output_docx_file)