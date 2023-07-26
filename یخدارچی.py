# یخدارچی
# https://quera.org/problemset/3429/

import os
os.system('cls' if os.name == 'nt' else 'clear')

def yakhdarchi(t):
    if t>100:
        print("Steam")
        
    elif t<0:
        print("Ice")
    else :
        print("Water")

t=int(input())

yakhdarchi(t)
