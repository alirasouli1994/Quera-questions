
a = ['shanbe' , '1shanbe' , '2shanbe' , '3shanbe' , '4shanbe' , '5shanbe' , 'jome']
b = 7
c = []

q = int(input())
x = []
x = input().split()

for i in range(0,q) :
    if x[i] not in c :
        c.append(x[i])

w = int(input())
y = []
y = input().split()

for i in range(0,w) :
    if y[i] not in c :
        c.append(y[i])

e = int(input())
z = []
z = input().split()

for i in range(0,e) :
    if z[i] not in c :
        c.append(z[i])

B = len(c)

print(b-B)

