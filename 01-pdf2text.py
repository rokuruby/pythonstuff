import PyPDF2

# Open the PDF file in read-binary mode
with open('/media/teong/7D65-FB09/python_stuff_experiment/PLACEHOLDER.pdf', 'rb') as file:
    # Create a PDF object
    pdf = PyPDF2.PdfFileReader(file)
    
    # Iterate over every page in the PDF
    for page in range(pdf.getNumPages()):
        # Extract the text from the page
        text = pdf.getPage(page).extractText()
        
        # Write the text to a file
        with open('output.txt', 'a') as f:
            f.write(text)
