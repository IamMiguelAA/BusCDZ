import codecs

ini = '<table class="tablePanel" style="width: 100%;">'
end = '</table>'
cont1 = 0
line_occur1 = []

dest = '<td>'
minutes = '<td style="text-align: center">'
lineabus = '<td id='

lineasdebus =[]
destinos =[]
llegadas=[]


with open('/Users/angoglez/Desktop/BUSCDZ/busNew.txt') as f:
    for line in f:
        cont1+=1
        if ini in line:
            line_occur1.append(cont1)

            for line in f:
                cont1+=1
                if end in line:
                    line_occur1.append(cont1)



newlines = open('/Users/angoglez/Desktop/BUSCDZ/busNew.txt').readlines()
with open('/Users/angoglez/Desktop/BUSCDZ/solotabla.txt', 'w+') as f2:

    f2.writelines(newlines[line_occur1[0]-1:line_occur1[1]])
    f2.seek(0)

    while True:
        line = f2.readline()
        if lineabus in line:
            line = f2.readline()
            lineasdebus.append(line)

        if dest in line:
            line = f2.readline()
            destinos.append(line)

        if minutes in line:
            line = f2.readline()
            llegadas.append(line)
        if not line: break

    lineasdebus = [x.replace('\r\n','') for x in lineasdebus]
    destinos = [x.replace('\r\n','') for x in destinos]
    llegadas = [x.replace('\r\n','') for x in llegadas]
    lineasdebus = [x.replace(' ','') for x in lineasdebus]
    destinos = [x.replace(' ','') for x in destinos]
    llegadas = [x.replace(' ','') for x in llegadas]

text='\n'

for i in range(0,len(lineasdebus)):
    text = text+lineasdebus[i]+'    '+destinos[i]+'    '+llegadas[i]+'\n'

print text

result = text




