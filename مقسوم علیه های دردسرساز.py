a = int(input())
n = 0
s = 0
for i in range(1,a+1):
    for j in range(1,i+1):
        if i%j==0:
            n += 1
            s += j
print(n, s)