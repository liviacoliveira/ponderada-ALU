import PyPDF2
reader = PyPDF2.PdfReader(r'c:\Users\Inteli\Downloads\ALU.pdf')
with open(r'c:\Users\Inteli\Desktop\eu\Inteli\ENG COMP - M05\ponderada-ALU\pdf_content.txt', 'w', encoding='utf-8') as f:
    for page in reader.pages:
        f.write(page.extract_text() + '\n')
