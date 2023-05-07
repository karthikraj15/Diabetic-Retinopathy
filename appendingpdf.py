from fpdf import FPDF
from PIL import Image
import glob
import os

def process(srcfname,destfname,msg,treat,pid,pname,age,gender):
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
    pdf.cell(40,10,gender,0,1,'c')
    pdf.cell(40,10,'   ',0,1,'c')
    pdf.cell(40,10,'You have been Diagnosed with ',0,1,'c')
    pdf.cell(40,10,msg,0,1,'c')
    pdf.cell(40,10,'   ',0,1,'c')
    pdf.multi_cell(pdf.w - 10,10,'Please consult your medical professional for follow up steps : ',0,1,'c')
    cell_width = pdf.get_string_width(treat) + 6
    if cell_width > pdf.w:
        cell_width = pdf.w - 10
    pdf.multi_cell(cell_width, 10, treat)
    
    path='./output/'+str(srcfname)+'/'+srcfname+"final.pdf"
    pdf.output(path, 'F')
    print("Final Pdf Created")


