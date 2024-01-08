n = int(input())
a = [int(i) for i in input().split()]
m = max(a)
print(a.index(m)+1)