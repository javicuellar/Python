import os
from PyPDF2 import PdfReader
import pandas as pd



def pdf_to_text():
    pdf_file = "01_Convertir_pdf_pandas.pdf"
    text = ""
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num in range(len(reader.pages)):
            page_text = reader.pages[page_num].extract_text()
            text += page_text
    return text


def pdf_to_excel(output_file):
    text = pdf_to_text()
    lines = text.split('\n')
    df = pd.DataFrame(lines)
    df.to_excel(output_file, index=False, header=False)


# Example usage:
output_excel_file = "01_Convertir_pdf_pandas.xlsx"

pdf_to_excel(output_excel_file)