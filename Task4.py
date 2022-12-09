# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k(до 6 степени).*
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int( input('Введите k: ') )

xarr = []
res = ''

for i in range(k + 1):
    xarr.append('{:+}'.format( random.randint(-100, +100) ) )

x = 1
y = 1
z = 0

for k in range(k,0,-1):
    if k <= 1:
        x = 0
    if k == 0:
        y = 0
    res += xarr[z] + y * ('x' + x * ('^' + str(k) + ' '))
    z += 1
res += ' = 0'

f = open('task4.txt', 'w')

if res[0] == '+':
    f.write(res[1:])
    f.write('\n')
else:
    f.write(res)
    f.write('\n')

f.close()