# عدد چاپ کن
# https://quera.org/problemset/9774/

a = input()
L = len(a)
ar=a[::-1]

for i in range(L):
    print(a[i],': ',sep='',end='')
    i=int(a[i])
    j=i
    while i>0:
        print(j,end='')
        i -=1
    print()


