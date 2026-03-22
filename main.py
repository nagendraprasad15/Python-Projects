import os
from docx2pdf import convert
from pdf2docx import Converter

choice = input("1. word to pdf or 2. pdf to word")

if choice == "1":
    file = input("Enter .docx file")
    if os.path.exists(file):
        convert(file,"output.pdf")
        print("converted word to pdf successfully")
    else:
        print("file not found")
elif choice == "2":
    file = input("enter pdf file path")
    if os.path.exists(file):
        cv = Converter("input.pdf")
        cv.convert("output.docx")
        cv.close()
        print("Converted PDF to Word Successfully")

    else:
        print("file not found")
else:
    print("Invalid choice")