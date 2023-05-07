from fpdf import FPDF
from PIL import Image
import glob
import os
def process(pid,pname,age,gen):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(40, 10, 'Diabetic Retenopathy Diagnose Report!',0,1,'c')
    pdf.cell(40, 10, 'Patient Id:',0,0,'c')
    pdf.cell(40,10,pid,0,1,'c')
    pdf.cell(40, 10, 'Patient Name:',0,0,'c')
    pdf.cell(40,10,pname,0,1,'c')
    pdf.cell(40, 10, 'Patient Age:',0,0,'c')
    pdf.cell(40,10,age,0,1,'c')
    pdf.cell(40, 10, 'Gender:',0,0,'c')
    pdf.cell(40,10,gen,0,1,'c')
    
    outpath='./output/'+pname+'/'
    if not os.path.isdir( outpath ) :
        os.mkdir( outpath )
    path='./output/'+str(pname)+'/' + pname+'.pdf'
    pdf.output(path, 'F')
    print("Pdf Created")
#process('p1','eswar','3','Male')
