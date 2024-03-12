import PyPDF2
import sys
import os


merger=PyPDF2.PdfMerger()
# pdffilemerger was the old function

for file in os.listdir(os.curdir):
    if file.endswith(".pdf"):
        print(file)
        merger.append(file)
        
merger.write("combinedpdf.pdf")
merger.close
