# Metode for automatisk å legge inn {} rundt store bokstaver i tittel.

import re
from subprocess import call
call(["cp", "bibl.bib", "bibllowcase.bib"])

r = open('bibllowcase.bib', 'r')
w = open('bibl.bib', 'w')

def addpar(line):
    line = line.replace('{', '')    
    line = line.replace('}', '')    
    line = line.replace('A', '{A}')
    line = line.replace('B', '{B}')
    line = line.replace('C', '{C}')
    line = line.replace('D', '{D}')
    line = line.replace('E', '{E}')
    line = line.replace('F', '{F}')
    line = line.replace('G', '{G}')
    line = line.replace('H', '{H}')
    line = line.replace('I', '{I}')
    line = line.replace('J', '{J}')
    line = line.replace('K', '{K}')
    line = line.replace('L', '{L}')
    line = line.replace('M', '{M}')
    line = line.replace('N', '{N}')
    line = line.replace('O', '{O}')
    line = line.replace('P', '{P}')
    line = line.replace('Q', '{Q}')
    line = line.replace('R', '{R}')
    line = line.replace('S', '{S}')
    line = line.replace('T', '{T}')
    line = line.replace('U', '{U}')
    line = line.replace('V', '{V}')
    line = line.replace('A', '{A}')
    line = line.replace('W', '{W}')
    line = line.replace('X', '{X}')
    line = line.replace('Y', '{Y}')
    line = line.replace('Z', '{Z}')
    line = line.replace('{{', '{')
    line = line.replace('}}', '}')
    line = line.replace('{{', '{')
    line = line.replace('}}', '}')
    line = line.replace('}{', '')
    line = line.replace('title = ', 'title = {')    
    line = line.replace(',\n', '},\n')    
    return line

title = re.compile('title =')
for line in r:
    res = title.findall(line)
    if (len(res) > 0.5):
        line = addpar(line)
        print(line)
    w.write(line)

r.close()
w.close()
call(["mv", "bibllowcase.bib", "old/"])




