# چاپ برعکس
# https://quera.org/problemset/3405/

# import os
# os.system('cls' if os.name == 'nt' else 'clear')

n=1
a=[]
while n!=0:
    n=int(input())
    a.append(n)

a.reverse()
for i in range(1,len(a)):
    print(a[i])

