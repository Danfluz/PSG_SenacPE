arquivo = open('texto1.txt', 'r')
substituicao = ''

for line in arquivo:
    if line.strip('\n') == 'linha2':
        substituicao = line.replace(line, 'novotexto\n')

arquivo.close()
fout = open('texto1.txt', 'w')
fout.write(substituicao)
fout.close()