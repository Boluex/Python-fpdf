from fpdf import FPDF,XPos,YPos
from PIL import ImageFont,Image,ImageDraw,ImageFilter



name='''
Greek art is renowned for its beauty, realism, and idealization of the human form. It emerged in the 8th century BCE and evolved over several centuries, producing some of the most iconic works of art in history.

Greek art can be divided into several periods, including the Geometric period, Archaic period, Classical period, and Hellenistic period. During the Geometric period, Greek art was characterized by abstract, geometric designs on pottery and other objects. The Archaic period saw the development of the kouros, a stylized, standing male figure, and the kore, a standing female figure. These figures were highly stylized and idealized, with exaggerated proportions and rigid poses.

The Classical period, which lasted from the 5th to 4th century BCE, is considered the pinnacle of Greek art. It was during this time that artists perfected the depiction of the human form, creating sculptures that were both realistic and idealized. The most famous example of this is the Parthenon, a temple dedicated to the goddess Athena in Athens. The Parthenon is considered the epitome of classical architecture and art, with its beautiful marble columns, pediments, and friezes depicting scenes from Greek mythology.

The Hellenistic period, which followed the Classical period, saw the rise of a more emotional and dramatic style of art. Artists focused on creating sculptures that were more realistic and expressive, with a greater emphasis on movement and emotion. Some of the most famous sculptures from this period include the Nike of Samothrace and the Laocoön and His Sons.

Greek art had a profound influence on Western art and culture, and its legacy can still be seen today. From ancient Roman copies of Greek sculptures to the neoclassical architecture of the 18th and 19th centuries, Greek art has left an indelible mark on the world of art and aesthetics. Its emphasis on the beauty and perfection of the human form, as well as its celebration of mythology and history, continues to inspire artists and viewers alike.
Greek architecture is renowned for its beauty, harmony, and sophistication. It emerged in the 8th century BCE and evolved over several centuries, producing some of the most iconic buildings in history.

Greek architecture can be divided into several styles, including the Doric, Ionic, and Corinthian orders. The Doric order, which originated in the 7th century BCE, is characterized by simple, sturdy columns with no base and a plain capital. The Ionic order, which emerged in the 6th century BCE, is characterized by more slender columns with a decorative base and volutes (scroll-shaped ornamentation) on the capital. The Corinthian order, which appeared in the 5th century BCE, is characterized by slender columns with an elaborate capital consisting of acanthus leaves.

Greek temples were the most prominent buildings in Greek architecture. They were typically rectangular in shape, with a row of columns on the front and back (the portico) and on the sides (the colonnade). The most famous example of Greek temple architecture is the Parthenon, a temple dedicated to the goddess Athena in Athens. The Parthenon is considered the epitome of classical architecture, with its beautiful marble columns, pediments, and friezes depicting scenes from Greek mythology.

Other notable examples of Greek architecture include the Theatre of Dionysus, a massive outdoor theater in Athens that could hold up to 17,000 spectators, and the Propylaea, a monumental gateway leading to the Acropolis in Athens.

Greek architecture had a profound influence on Western architecture and culture, and its legacy can still be seen today. From ancient Roman copies of Greek buildings to the neoclassical architecture of the 18th and 19th centuries, Greek architecture has left an indelible mark on the world of architecture and aesthetics. Its emphasis on balance, proportion, and harmony, as well as its celebration of mythology and history, continues to inspire architects and viewers alike.
'''



from fpdf import FPDF

class MyPDF(FPDF):
    def header(self):
        # Add a background image to the header of each page
        self.image('/home/deji/Desktop/deji/PycharmProjects/pythonProject/connecto.png', x=0, y=0, w=self.w, h=self.h)
        
    def add_content(self, my_variable):
        # Set the font and font size for the text
        self.set_font('Arial', '', 12)
        # Add a multicell to the PDF document
        self.multi_cell(0, 10, my_variable, border=0, align='J', fill=0)

def create_pdf(filename, variable):
    # Create a PDF object
    pdf = MyPDF('P', 'mm', 'A4')

    # Add a page to the PDF document
    pdf.add_page()

    # Call the add_content method to add content to the PDF document
    pdf.add_content(variable)

    # Save the PDF document
    pdf.output(filename)

# Call the create_pdf function to create the PDF document
create_pdf('output.pdf', name)
