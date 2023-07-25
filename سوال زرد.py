#صورت سوال
# https://quera.org/contest/assignments/923/problems/3363



import os
os.system('cls' if os.name == 'nt' else 'clear')
def wow(j):
    n = {}
    n=["W", "o", "w", "!"]

    for i in range(j-1):
        n.insert(1,"o")
    
    print("".join(n))

n=int(input())
wow(n)
