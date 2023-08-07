# بهداشت و سلامت
# https://quera.org/problemset/51865/

X = int(input())
N = int(input())

if N == 0 :
    X = 20
    print(X)
else:
    if N == 7 :
        print(X)
    else:
        X = X - N
        if X < 0 :
            print(0)
        else:
            print(X)