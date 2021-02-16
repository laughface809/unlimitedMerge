import PyPDF2
import sys

#inputs = sys.argv[1:] # From input (without spaces!)
inputs = ['test 1.pdf', 'test 2.pdf'] # Add those pdf's to your project

def pdf_combine(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merge.pdf')

pdf_combine(inputs)
