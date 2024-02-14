f = open('space.txt', 'r', encoding='utf-8')
l = f.readline() #строчка названий
a = [] #список, в котором будут записаны строки из файла
for i in f:
    b = (i.strip().split('*')) #временная переменная, через которую строки записываются в а
    b[0] = [b[0].split('-')[0], b[0].split('-')[1]]
    b[2] = list(map(int, b[2].split()))
    b[3] = list(map(int, b[3].split()))
    a.append(b)

f1 = open('space_new.txt', 'w', encoding='utf-8')
f1.write(l)
for i in a:
    n = int(i[0][1][0])
    m = int(i[0][1][1])
    t = len(i[2]) - i[2].count(' ')
    xd = i[3][0]
    yd = i[3][1]
    #переменные создаются по описанию из условия

    if n > 5:
        x = n + xd
    else:
        x = -(n + xd) * 4 + t
    if m > 3:
        y = m + t + yd
    else:
        y = -(n + yd) * m

    shipname = i[0][0] + '-' + i[0][1]
    planet = i[1]
    coord = str(x) + ' ' + str(y)
    direction = str(i[3][0]) + ' ' + str(i[3][1])
    #временные переменные для записи необходимых значений в новый файл
    f1.write(f'{shipname}*{planet}*{coord}*{direction}\n')

    if i[0][0][-1] == 'V':
        print(i[0][0] + '-' + i[0][1] + ' - (' + str(x) + ', ' + str(y) + ')')

f1.close()