with open('/mnt/dados/projetos/variables.data', 'r') as file:
    code_lines = file.readlines()

for cl in code_lines:
    exec(cl)