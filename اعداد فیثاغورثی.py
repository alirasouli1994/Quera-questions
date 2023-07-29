# اعداد فیثاغورثی
# https://quera.org/problemset/280/

import os
os.system('cls' if os.name == 'nt' else 'clear')

def fisha(b):
    a = sorted(b)   
    if 1<=a[0] and 1<=a[1] and 1<=a[2] and a[0]<=150 and a[1]<=150 and a[2]<=150:
        if a[0]**2+a[1]**2==a[2]**2:
            return "Yes"
        else:
            return "No"

a= []
a.append(int(input()))
a.append(int(input()))
a.append(int(input()))

print(fisha(a))

