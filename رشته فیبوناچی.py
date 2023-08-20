a = int(input())
fib = [ 1 , 2]
# i=int(len(fib))
i = 2
print('+',end='')
while i <= a :
    fib.append(fib[i - 1] + fib[i - 2])
    if i in fib:
        print('+',end='')

    else:
        print('-',end='')
    i +=1

