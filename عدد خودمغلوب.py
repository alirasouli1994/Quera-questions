# عدد خود مغلوب
# https://quera.org/problemset/617/
n=int(input())
a=[]
b=[]
while n>0:
   a.append(n%10)
   n=n//10
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
if a==b:
    print("YES")
else:
    print("NO")