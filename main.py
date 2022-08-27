from docx import Document

document = Document('./src/sample.docx')

quiz = {
    'name': '',
    'questions': [],
}

for p in document.paragraphs:
    if p.style.name == 'Heading 1':
        quiz['name'] = p.text
    elif p.style.name == 'Heading 2':
        quiz['questions'].append({
            'body': p.text
        })

print(quiz)
