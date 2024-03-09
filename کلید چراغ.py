n = int(input())
a=[]
for i in range(n):
    a += [int(input())]
b = 0
j = a[0]
for i in range(1,len(a)):
    if a[i] != j :
        b += 1
        j = a[i]
print(b)