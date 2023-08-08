from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font('helvetica', size=50)
pdf.cell(0, 30, 'CS50 Shirtificate', align='C')
pdf.image("shirtificate.png", x=10, y=80, w=180)
name = input("Name: ")
pdf.set_text_color(255, 255, 255)
pdf.set_x(0)
pdf.set_font('helvetica', size=25)
pdf.cell(0, 240, txt=f"{name} took CS50", align='C')
pdf.output("shirtificate.pdf")