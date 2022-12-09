# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.*
# Пример:

# - 2*x² + 4*x + 5 = 0 
# - 5*x² + 2*x + 43 = 0
# - Результат: 7*x^2 + 6*x + 48 = 0

# *Значения коэффициентов от -100 до 100
# *Сумма многочленов с разными степенями
# Пример:
# - 2*x^2 + 4*x + 5 = 0
# - 5*x^4 + 2*x^3 - 6*x^2 + 13*x + 43 = 0
# - Результат: 5*x^4 + 2*x^3 - 4*x^2 + 17*x + 48 = 0

import re

def ReadExp(file):
    f = open(file, 'r')
    res = f.readline().replace(' ','').replace('=0','')
    
    if res[0] != '-':
        res = '+' + res

    f.close()
    return res

def addRes(n, v):
    n = int(n)
    v = int(v)
    if ( res.get(n) ):
        res.update( { n: res.get(n) + v } )
    else:
        res.update( { n: v } )

def analyze(match):
    regex = re.compile(r'([+-]\d+)(\*x(?:\^(\d+))?)?')
    
    for item in match:
        v = regex.findall( item )[0]

        if (v[2]=='' and v[1]==''):
            n = 0
        elif (v[2]==''):
            n = 1
        else:
            n = v[2]
        addRes(n, v[0])

res = {}

exp1 = ReadExp('task5_in1.txt')
exp2 = ReadExp('task5_in2.txt')

regex = re.compile( r'([+-]\d+(?:\*x)?(?:\^\d+)?)' )
match1 = regex.findall(exp1)
match2 = regex.findall(exp2)

analyze(match1)
analyze(match2)

for n,v in res.items():
    print( '{:+}'.format(v), end='' )
    if (n > 1):
        print('x^'+str(n), end='')
    elif (n == 1):
        print('x', end='')

print('=0')