import webbrowser
from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period

class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a Pdf file that contains data about the flatmates such as their names, their due amounts and the period of the bill.
    """
    
    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        pdf.set_font(family='Times', size=24, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", align="C", ln=1)

        pdf.set_font(family='Times', size=18, style="B")
        pdf.cell(w=100, h=40, txt="Period:")
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        pdf.set_font(family='Times', size=16)
        pdf.cell(w=100, h=40, txt=flatmate1.name)
        pdf.cell(w=150, h=40, txt=flatmate1_pay, ln=1)
        pdf.cell(w=100, h=40, txt=flatmate2.name)
        pdf.cell(w=150, h=40, txt=flatmate2_pay, ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
        
the_bill = Bill(amount=100, period="April 2021")
bob = Flatmate(name="Bob", days_in_house=7)
mary = Flatmate(name="Mary", days_in_house=10)
report = PdfReport(filename="bill.pdf")
report.generate(flatmate1=bob, flatmate2=mary, bill=the_bill)
