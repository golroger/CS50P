#golroger
from fpdf import FPDF
from PIL import Image, ImageOps

def main():
    x = input("Name:")
    pdftext(x)

def pdftext(x) :
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.set_auto_page_break(auto=False)
    pdf.add_page("portrait","a4")
    # text one
    pdf.set_font("Arial",'', size = 48)
    pdf.cell(0, 40 , "CS50 Shirtificate",align="C")
    # image
    pdf.image("shirtificate.png", h=pdf.eph * 0.7 ,  x= 4, y =85)

    # text 2
    pdf.set_font("Arial",'', size = 24)
    pdf.set_text_color(r=255, g=255, b=255)
    pdf.ln(140)
    pdf.cell(0, 0 , x + " took CS50",align="C")

    # create the pdf
    pdf.output("shirtificate.pdf")

if __name__ == "__main__" :
    main()
