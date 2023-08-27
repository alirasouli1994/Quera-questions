a=[1 ,1 ,2 ,2 ,2 ,8 ]
b = [int(i) for i in input().split()]
for j in range(len(a)):
    print(a[j]-b[j],end=' ')