def is_prime(n):
    for i in range (2,int(n**0.5)+1):
        if n % i == 0 :
            return False
    return True

a =int(input())
b =int(input())
c=[]
for i in range(a+1,b):
    if is_prime(i):
        c += [i]

str_c= [str(i) for i in c]
b = ",".join(str_c)
print(b)