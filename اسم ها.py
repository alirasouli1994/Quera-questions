def namelen(a):
    b = ''
    for i in a:
        if i not in b :
            b += i
    return(len(b))
n = int(input())
m = 0
for i in range(n):
    a = input()
    b = namelen(a)
    
    if int(b) > m:
        m = b
print(m)