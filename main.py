from docx import Document

document = Document('./src/sample.docx')

quiz = {}

for p in document.paragraphs:
    if p.style.name == 'Heading 1':
        quiz['name'] = p.text

print(quiz)
