# مشق امشب باقر
# https://quera.org/problemset/10230/

import os
os.system('cls' if os.name == 'nt' else 'clear')

def rectangle(x, y, z) :
    
    if 0<x<180 and 0<y<180 and 0<z<180 :

        if x+y+z == 180:
            print ("Yes")
        else: 
            print ("No")

    else:
        print ("No")

x, y, z = map(int, input().split())

rectangle(x, y, z)
