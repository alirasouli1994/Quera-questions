# تک رقمی
# https://quera.org/problemset/3539/

a = input()
L = len(a)
x = 0
while L > 1 :
    for i in range (L):
        y = int(a[i])
        x = x + y
    a = str(x)
    x = 0
    L = len(a)
print(a)