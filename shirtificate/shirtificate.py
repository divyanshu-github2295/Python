from fpdf import FPDF


class shirtificate:

    # Constructor
    def __init__(self, name):
        self.name = name

    # Making Shirtificate
    def make_shirtificate(self):

        # Instance of FPDF class
        make_pdf = FPDF(unit="mm")
        # Adding Page
        make_pdf.add_page(orientation="P", format="A4")
        # Set font for Title
        make_pdf.set_font("courier", "B", 35)
        # Adding Title on the page
        make_pdf.cell(0, 35, "CS50 Shirtificate", new_x="LEFT", new_y="NEXT", align="C")
        # Adding Image of shirt on page
        make_pdf.image("shirtificate.png", 5, 45, 198)
        # Text colour: White
        make_pdf.set_text_color(255, 255, 255)
        make_pdf.set_font("courier", "B", 21)
        # Printing Student Name on shirt
        make_pdf.cell(0, 135, f"{self.name} took CS50", align="C")
        # Making pdf
        make_pdf.output("shirtificate.pdf")


def main():

    # Getting name of student
    name = input("Name: ")

    # Class Instance
    shirt = shirtificate(name)
    # Calling method in class for creating Shirtificate
    shirt.make_shirtificate()


if __name__ == "__main__":
    main()
