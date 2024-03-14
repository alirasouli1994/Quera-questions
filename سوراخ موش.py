x1 , x2 = map(int,input().split())
if x1 == x2 :
    print("Saal Noo Mobarak!")
if x1 < x2 :
    for i in range (x2-x1):
        print("R",end='')
if (x1 > x2):
    for i in range(x1-x2):
        print("L",end='')