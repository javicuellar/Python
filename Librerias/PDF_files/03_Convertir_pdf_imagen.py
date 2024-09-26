import os
from PyPDF2 import PdfReader
from pdf2image import convert_from_path


def pdf_to_images(pdf_file, output_dir):
    images = []
    with open(pdf_file, 'rb') as f:
        reader = PdfReader(f)
        for page_num, _ in enumerate(reader.pages):
            # Convert each PDF page to image
            img_path = os.path.join(output_dir, f"page_{page_num}.png")
            images.append(img_path)
    return images


# Example usage:
pdf_file = "03_Convertir_pdf_imagen.pdf"
output_dir = "03_Convertir_pdf_imagen"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

pdf_to_images(pdf_file, output_dir)