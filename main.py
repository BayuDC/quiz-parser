import docx
import yaml
import glob


def convert(filename):
    document = docx.Document(filename)

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

    with open(filename.replace('src', 'dist').replace('docx', 'yml'), 'w') as file:
        yaml.dump(quiz, file)


for filename in glob.glob('./src/*.docx'):
    convert(filename)
