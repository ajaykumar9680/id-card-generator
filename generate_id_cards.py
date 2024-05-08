import os
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import utils


def create_id_card(pdf_file, template_image, csv_file, photo_directory):
    #canvas object
    c = canvas.Canvas(pdf_file, pagesize=(3.375*inch, 2.125*inch))

    #template image loading
    template_path = os.path.join(os.getcwd(), template_image)
    template = utils.ImageReader(template_path)

    # reading info from csv file
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # default template we are using
            c.drawImage(template_path, 0, 0, width=3.375*inch, height=2.125*inch)

            #adding employee info
            c.setFont("Helvetica", 10)
            c.drawString(0.25 * inch,  1.2 * inch, f"Name: {row['name']}")
            c.drawString( 0.25 * inch,  0.90 * inch, f"Position: {row['position']}")

            #employee photo is loading
            photo_path = os.path.join(photo_directory, row['photo'])
            photo = utils.ImageReader(photo_path)
            c.drawImage(photo, 1.90 * inch, 0.8 * inch, width=1.15 * inch, height=1.00 * inch)

            #for every new page
            c.showPage()
    c.save()



if __name__ == "__main__":
    template_image = "id_template.png"
    csv_file = "employee_info.csv"
    photo_directory = "employee_photos"
    pdf_file = "employee_id_cards.pdf"

    create_id_card(pdf_file, template_image, csv_file, photo_directory)

    print("PDF file generated successfully")
