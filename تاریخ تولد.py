# تاریخ تولد
# https://quera.org/problemset/615/

n = int(input())
a=[]
for i in range(4):
    a.append(int(n%10))
    n=n//10
a.reverse()
print("saal:",a[0],a[1],sep="")
print("maah:",a[2],a[3],sep="")