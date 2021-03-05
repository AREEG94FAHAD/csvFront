# ###################################
# Help

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from PIL import Image
from reportlab.lib.colors import HexColor, white, Color, black
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus.frames import ShowBoundaryValue


def drawMyRuler(pdf):
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')


# ###################################
# Content
fileName = 'MyDoc.pdf'
documentTitle = 'Document title!'
name = 'Areeg Fahad Rasheed'
aboutme = " Areeg Fahad Rasheed Areeg Fahad Rasheed Network Engineer and Full Stack Developer with 2 + years of hands-on experience designing developing, implementing applications and solutions using a range of technologies and programming "
subTitle = 'The largest carnivorous marsupial'
back = ['Al-Nahrain University', 'M.S DEGREE IN SCIENCE OF NETWORK ENGINEERING',
        'Al-Iraqia University', 'B.A DEGREE IN NETWORK ENGINEERING',
        'Al-Iraqia University', 'B.A DEGREE IN NETWORK ENGINEERING']

experienceList = ['Lecture and lab instructor',
                  'Lecture in iraq baghdad and fddd dddd dddd sonice and lab instructor', 'Lecture and lab instructor']
contact = ['Mobile: ', ' 07714355819', 'Email', 'Fahedareeg@gmail.com', 'Facebook',
           'AreegFahadRasheed', 'WebSite', 'www.google.co,', 'Github', 'Areeg94fahad', 'Linkedin', 'areeg fahad']
SKILLS = [
    'Web development',
    'Computer network',
    'Data analysts',
    'security',
    'Prize',
    'Latex',
    'video and vice edditing',
    'searching',
    'Microsoft office',
    'handle with several type of OS'
]

certificate = ['Huawei Certified Network Associate (HCNA)','Huawei Certified Network Associate (HCNA)', 'Huawei Certified Network Associate (HCNA)',
               'Introduction to Computer Science (CS50)', 'Fundamentals of Digital marketing', 'Fundamentals of Digital marketing']
aco = ['Got a scholarship from huawei to get HCIA CERTIFICATE',
'Got a scholarship from huawei to get HCIA CERTIFICATE',
'Got a scholarship from huawei to get HCIA CERTIFICATE']

image = Image.open('tasmanianDevil.jpg')
new_image = image.resize((110, 90))


s = getSampleStyleSheet()
s = s["BodyText"]
s.wordWrap = 'CJK'

pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)


# Title Style
titile = ParagraphStyle('titile')
titile.firstLineIndent = 0
titile.textColor = HexColor(0xff8100)
titile.fontSize = 16


# text Style
text = ParagraphStyle('text')
text.firstLineIndent = 0
text.textColor = HexColor(0x6f8b80)
text.fontSize = 12
text.spaceBefore = 6
text.justifyBreaks = 1
text.justifyLastLine = 1
text.splitLongWords = 1


# bold
boldd = ParagraphStyle('boldd')
boldd.firstLineIndent = 0
boldd.textColor = HexColor(0x6f8b80)
boldd.fontSize = 12
boldd.spaceBefore = 6
boldd.borderPadding = 1
# boldd.leftIndent = 12
boldd.spaceAfter = 3


# Aboutme
story = []
story.append(Paragraph("ABOUT ME", titile))
story.append(Paragraph(aboutme, text))
f = Frame(27, 600, 300, 100)
f.addFromList(story, pdf)


# drawMyRuler(pdf)

pdf.setFillColor(HexColor(0xff8100))
pdf.setFont("Courier-Bold", 24)
pdf.drawCentredString(170, 725, name)

pdf.drawInlineImage(new_image, 440, 680)
pdf.setStrokeColor(white)

pdf.setLineWidth(30)
pdf.circle(495, 725, 60, stroke=1, fill=0)


# Eduction
story = []
story.append(Paragraph("ACADEMIC BACKGROUND", titile))
for i in range(0, len(back), 2):

    story.append(Paragraph(back[i], text))
    story.append(Paragraph(back[i+1], boldd))

ff = Frame(27, 445, 300, 150, showBoundary=1)
ff.addFromList(story, pdf)

# Experience
experience = []
experience.append(Paragraph("Experience", titile))
for i in range(len(experienceList)):
    experience.append(Paragraph(experienceList[i], boldd))
experiencef = Frame(27, 320, 300, 100)
experiencef.addFromList(experience, pdf)


# skils
skilss = []

skilss.append(Paragraph("SKILLS", titile))
for i in range(len(SKILLS)):
    skilss.append(Paragraph(SKILLS[i], boldd))
skilssf = Frame(27, 10, 300, 300)
skilssf.addFromList(skilss, pdf)

# certificaites
cer = []

cer.append(Paragraph("CERTIFICATES", titile))
for i in range(len(certificate)):
    cer.append(Paragraph(certificate[i], boldd))
cerf = Frame(340, 395, 300, 200)
cerf.addFromList(cer, pdf)






#contact
contactinfo = []
contactinfo.append(Paragraph("CONTACT", titile))
for i in range(0,len(contact),2):
    contactinfo.append(Paragraph(contact[i], boldd))

contactinfoff = Frame(340, 270, 150, 150)
contactinfoff.addFromList(contactinfo, pdf)



contactinfo = []
contactinfo.append(Paragraph("INFO", titile))
for i in range(1,len(contact),2):
    contactinfo.append(Paragraph(contact[i], text))

contactinfoff = Frame(422, 270, 250, 150)
contactinfoff.addFromList(contactinfo, pdf)


# ACCOMPLISHMENTS
acop = []

acop.append(Paragraph("ACCOMPLISHMENTS", titile))
for i in range(len(aco)):
    acop.append(Paragraph(aco[i], boldd))
acopf = Frame(340, 50, 300, 200)
acopf.addFromList(acop, pdf)


pdf.save()
