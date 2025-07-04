from fpdf import FPDF
def main():
    name=input("Name: ")
    make_tshirt(name)
def header(self):
        self.set_font("helvetica", style="", size=30)
        self.cell(80)
        self.cell(30, 30, "CS50 Shirtificate", border=0, align="C")
        self.ln(20)
def make_tshirt(name):
    pdf = FPDF()
    pdf.add_page(format=(210 ,297))
    pdf.image("./shirtificate.png",x=45, y=40, w=100, h=100)
    header(pdf)
    pdf.set_font("Helvetica",size=20)
    pdf.set_text_color(255,255,255)
    pdf.cell(180,100,f"{name} took CS50",align="C",)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()