import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path


filepaths = glob.glob("invoices/*.xlsx")
print(filepaths)

for filepath in filepaths:
    #Set the dataframe
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    #Set the page
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    #Get the invoice number
    filename = Path(filepath).stem     # Intelligent library and method to obtain the name of the file
    invoice_nr, date = filename.split("-")  # This way we obtain the "name" of the invoice, its number.

    # Write the text
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice nr. {invoice_nr}", ln=1) # ln=1 indicates a breakline

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{date}")

    #Create the pdfs
    pdf.output(f"PDFs/{filename}.pdf")