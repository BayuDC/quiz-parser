from math import fabs
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
            'body': p.text,
            'choices': []
        })
    elif p.style.name == 'normal':
        correct = False
        for r in p.runs:
            if r.bold == True:
                correct = True
                break

        quiz['questions'][-1]['choices'].append({
            'body': p.text,
            'correct': correct
        })


print(quiz)
