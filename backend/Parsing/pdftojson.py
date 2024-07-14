import PyPDF2
from .ResumeParser import ResumeParser
def get_resume_json(file):
    resumeText=""
    pdf_reader = PyPDF2.PdfReader(file)
    for page_number in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_number]
                page_text = page.extract_text()
                resumeText+=page_text
    print("going to ")
    resumeJSON = ResumeParser(resumeText).Groq()
    return resumeJSON

