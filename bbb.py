f = open('space.txt', 'r', encoding='utf-8')
l = f.readline() #строчка названий
a = [] #список, в котором будут записаны строки из файла
for i in f:
    b = (i.strip().split('*')) #временная переменная, через которую строки записываются в а
    b[2] = list(map(int, b[2].split()))
    b[3] = list(map(int, b[3].split()))
    a.append(b)
print(*a, sep='\n')

j = input('Введите название корабля: ')
while j != 'stop':
    tf = False
    for i in a:
        if i[0] == j:
            tf = True
            break
    if tf:
        print(f'Корабль {j} был отправлен с планеты: {i[1]} и его направление движения было: ({i[3][0]}; {i[3][1]})')
    else:
        print('error.. er.. ror..')
    j = input('Введите название корабля: ')