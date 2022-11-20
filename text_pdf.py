import PyPDF2

pdfFileObj = open('mypdf.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)

text = pageObj.extractText()

print(text)