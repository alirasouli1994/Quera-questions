# فاکتوریل
# https://quera.org/problemset/589/

import os
os.system('cls' if os.name == 'nt' else 'clear')

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input())

print(factorial(n))