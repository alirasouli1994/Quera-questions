#  چاپ مربع
# https://quera.org/problemset/591/

import os
os.system('cls' if os.name == 'nt' else 'clear')

n= int(input())
for i in range(n):
    for j in range(n):
        if i ==0 or i ==n-1 or j==0   or j ==n-1:
            print ("*",end='')
        else:
            print (" ",end='')
    print ("")

    

    
