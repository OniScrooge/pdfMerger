import PyPDF2
import sys
import os

merger = PyPDF2.PdfFileMerger()

for file in os.listdir(os.curdir):          # Opens file directory
    if file.endswith(".pdf"):               # Readies any file in file directory that is saved as a '.pdf'
        merger.append(file)                 # Concatenates those files using the append method
    merger.write("combinedBSUniDocs.pdf")