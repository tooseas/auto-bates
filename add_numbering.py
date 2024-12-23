from re import L
import pypdf

needsNumFile = open('Evidence.pdf', 'rb')                     #change name of file to file to be marked
pdfReader = pypdf.PdfReader(needsNumFile)

numberingFile = open('page_numbers.pdf', 'rb')
pdfNumberingReader = pypdf.PdfReader(numberingFile)
pdfWriter = pypdf.PdfWriter()

for pageNum in range (0, pdfReader.get_num_pages()):
    needsNumFilePage = pdfReader.get_page(pageNum)
    NumFilePage =pdfNumberingReader.get_page(pageNum)
    needsNumFilePage.merge_page(NumFilePage)
    pdfWriter.add_page(needsNumFilePage)

numberedFile = open ('numbered_file.pdf', 'wb')
pdfWriter.write(numberedFile)
needsNumFile.close()
numberingFile.close()
numberedFile.close()
