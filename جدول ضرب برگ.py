# جدول ضرب برگ
# https://quera.org/problemset/3409/

import os
os.system('cls' if os.name == 'nt' else 'clear')

def big_times(a):
    result = ''
    for i in range(1, a+1):
        for j in range(1, a+1):
            result += str(i*j) + ' '
        result += '\n'
    return result

a = int(input())
print(big_times(a))
