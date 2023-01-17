import re
import time

start = time.time()

f = open('timetable.yml', 'r', encoding="utf-8")
list = f.readlines()
f.close()

f1 = open('timetable2.xml', 'w', encoding="utf-8")

for line in list:

    line = re.sub('-','',line,1)

    for i in range(len(line)):
        if line[i] != ' ':
            s = i
            break
    if re.search(':',line):
        line = line[:s] + '<' + line[s:]

    line = re.sub(' ','\t',line,s)

    if re.search(':',line):
        line = re.sub(':\s*','>',line,1)

    tag1 = re.search('<\w+>',line)
    tag = tag1[0]

    if line[len(line)-1] != '>':
        line = line[0:len(line)-1] + '</' + tag[1:] + '\n'
    else:
        line = line + '\n'

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