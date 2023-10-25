from PyPDF2 import PdfReader


def pdf_to_string(file_path):
    reader = PdfReader(file_path)

    whole_page_text = ""

    for page_number in range(0, len(reader.pages)):
        page = reader.pages[page_number]
        page_text = page.extract_text()
        whole_page_text += page_text

    return whole_page_text

def _save_text():
    text = pdf_to_string('./sample_pdf/birgunj.pdf')
    with open('./test.txt', 'w') as f:
        f.write(text)

if __name__ == '__main__':
    _save_text()