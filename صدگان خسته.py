# صدگان خسته
# https://quera.org/problemset/3406/

A = input()
B = input()

Ar = A[::-1]
Br = B[::-1]
a = int(Ar)
b = int(Br)

if a < b :
    print(A,' < ', B)
elif a == b :
    print(A, ' = ', B)
else:
    print(B,' < ', A)
