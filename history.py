import pdfplumber
from gtts import gTTS
def get_pdf_file():  
    file_path="history.pdf"
    with pdfplumber.PDF(open(file_path, mode='rb')) as pdf_file:
        pages = pdf_file.pages
        pages_pdf_text = ''.join([page.extract_text() for page in pages])
        pdf_file = pages_pdf_text.replace("\n", "")
    return pdf_file

   
def get_audio_file(pdf_file):
    language = "ru"
    phrase = gTTS(text=pdf_file, lang=language, slow=False)
    phrase.save("audio_file.mp3")
    

def main():
    pdf_file = get_pdf_file()
    get_audio_file(pdf_file)


if __name__ == '__main__':
    main()