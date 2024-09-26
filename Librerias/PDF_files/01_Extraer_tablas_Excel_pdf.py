#    Extraido de twitter clcoding
#   -------------------------------
#  Convertir fichero PDF a Excel
#
#  Necesario instalar pdfplumber, pandas y openpyxl

import pdfplumber
import pandas as pd


def pdf_to_excel(pdf_file, excel_file):

    with pdfplumber.open(pdf_file) as pdf:
        all_tablas = []
        for page in pdf.pages:
            tablas = page.extract_tables()
            for tabla in tablas:
                if tabla:
                    df = pd.DataFrame(tabla)
                    all_tablas.append(df)
        
        if not all_tablas:
            all_tablas.append(pd.DataFrame([['No se han encontrado tablas']]))
        
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            for idx, df in enumerate(all_tablas):
                df.to_excel(writer, sheet_name=f'Sheet{idx + 1}', index=False)

pdf_to_excel('01_Extraer_tablas.pdf', '01_Extraer_tablas.xlsx')
