import time
start = time.time()

f = open('timetable.yml', 'r', encoding="utf-8")
list = f.readlines()
f.close()

f1 = open('timetable.xml', 'w', encoding="utf-8")

for line in list:

    line = line.replace('-','',1)

    for i in range(len(line)):
        if line[i] != ' ':
            s = i
            break
    if line.find(":"):
        line = line[0:s] + '<' + line[s:len(line)]

    line = line.replace(' ','\t',s)

    if line.find(":"):
        line = line.replace(': ',':',1)
        line = line.replace(':','>',1)

    if line.find('<') != -1:
        s1 = line.find('<')
        s2 = line.find('>')

    tag = line[s1+1:s2]

    if line[len(line)-2] != '>':
        line = line[0:len(line)-1] + '</' + tag + '>' + '\n'

    if line.find("lesson2") != -1:
        f1.write('\t</lesson1>\n')

    if line.find("lesson3") != -1:
        f1.write('\t</lesson2>\n')

    f1.write(line)

f1.write('\t</lesson3>\n')
f1.write('</timetable>\n')
f1.close()

end = time.time()

print((end - start)*100)