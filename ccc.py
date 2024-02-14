import csv
f = open('space.txt', 'r', encoding='utf-8')
l = f.readline() #строчка названий
a = [] #список, в котором будут записаны строки из файла
for i in f:
    b = (i.strip().split('*')) #временная переменная, через которую строки записываются в а
    b[0] = [b[0].split('-')[0], b[0].split('-')[1]]
    b[2] = list(map(int, b[2].split()))
    b[3] = list(map(int, b[3].split()))
    a.append(b)
l += ';password'
with open('space_uniq_password.csv', 'w', encoding='utf-8') as f1:
    f1.write(l.replace('*', ';'))
    for i in a:
        shipname = i[0][0] + '-' + i[0][1]
        planet = i[1]
        coord = str(i[2][0]) + ' ' + str(i[2][1])
        direction = str(i[3][0]) + ' ' + str(i[3][1])
        password = (i[1][-3:] + i[0][0][2:0:-1] + i[1][2:0:-1]).upper()
        #временные переменные для записи необходимых значений в новый файл
        f1.write(f'{shipname};{planet};{coord};{direction};{password}')

f1.close()
