# para cada arquivo em `templates/full-templates`...

import os

files = os.listdir('templates/full-templates')

jsonOutput = {}

for file in files:
    with open(f'templates/full-templates/{file}', 'r') as f:
        # pegar a 7ª linha do arquivo
        lines = f.readlines()
        linha7 = lines[6].strip()

        jsonOutput[linha7] = file

print(jsonOutput)
