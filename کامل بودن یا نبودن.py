# کامل بودن یا نبودن 
# https://quera.org/problemset/282/

import os
os.system('cls' if os.name == 'nt' else 'clear')


def kamel(a):
    
    # if a>11:
    #     a=int(a/2)
    
    sum=0
    for i in range(1,a):
        if a%i == 0:
            sum=sum+i
    if sum == a:
        return 'YES'
    else:
        return 'NO'

n=int(input())
print(kamel(n)) 