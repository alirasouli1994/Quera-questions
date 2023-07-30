# دونقطه خط
# https://quera.org/problemset/3414/

import os
os.system('cls' if os.name == 'nt' else 'clear')

emploee={}
emploee["x"] =[]
emploee["y"] =[]
bass={}
bass["x"] =[]
bass["y"] =[]

emploee["x"],emploee["y"],bass["x"],bass["y"] =map(int,input().split())

if emploee["x"]==bass["x"]:
    print("Vertical")
elif emploee["y"]==bass["y"]:
    print("Horizontal")
else:
    print("Try again")




