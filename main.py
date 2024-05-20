import os
import PyPDF2

# Set the path to the folder containing the PDF files
pdf_folder = 'path/to/folder'

# Loop through all PDF files in the folder
for filename in os.listdir(pdf_folder):
    if filename.endswith('.pdf'):
        # Open the PDF file in read binary mode
        with open(os.path.join(pdf_folder, filename), 'rb') as pdf_file:
            # Read the PDF file using PyPDF2
            pdf_reader = PyPDF2.PdfFileReader(pdf_file)
            # Extract the text from each page of the PDF file
            text = ''
            for page_num in range(pdf_reader.getNumPages()):
                page = pdf_reader.getPage(page_num)
                text += page.extractText()
            # Save the text as a separate TXT file in the same folder
            with open(os.path.join(pdf_folder, filename[:-4] + '.txt'), 'w') as txt_file:
                txt_file.write(text)