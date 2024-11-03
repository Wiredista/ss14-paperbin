# open `documentos.txt`
documentos = open('documentos.txt', 'r')

templates = {}

import re
while True:
    line = documentos.readline()
    if not line:
        break
    rexp = re.compile(r'doc-text-printer-(\w+) =')
    match = rexp.match(line)
    if match:
        print(f"Reading {match.group(1)}")
        template_name = match.group(1)
        template_text = ''
        while True:
            line = documentos.readline()
            if not line.startswith('doc-text-printer'):
                template_text += line
            else:
                break
            
        # remove the first 7 lines
        template_text = '\n'.join(template_text.split('\n')[7:])

        templates[template_name] = template_text


for key, value in templates.items():
    with open(f'templates/full-templates/{key}.txt', 'w') as f:
        f.write(value)

documentos.close()