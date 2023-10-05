import PyPDF2
pdfFiles = ["1.pdf", "2.pdf", "3.pdf"]
merger = PyPDF2.PdfMerger()
for fname in pdfFiles:
    pdfFile = open(fname, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()
merger.write("pdf-merged.pdf")



