from PyPDF2 import PdfFileMerger
def process(uname):
    path = './output/'+str(uname)+'/'
    pdfs = [path + uname+'final.pdf', path +uname+'output.pdf']

    merger = PdfFileMerger()
    cnt = 1
    for pdf in pdfs:
        if cnt == 1:
            merger.append(pdf,pages=(0,1))
            cnt = 0
        else:
            merger.append(pdf)


    merger.write(path + uname+"result.pdf")
    merger.close()

