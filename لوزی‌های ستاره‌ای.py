n =int(input())
n =int( (n/2)+0.5)
for i in range (1,n+1) :
    up_star_L = ' ' * (n-i) + '*' * ((2*i)-1)
    up_star_R = (' '*(n-i))+(' ' * (n - i) + '*' * ((2 * i) - 1))
    print(up_star_L,up_star_R,sep='')
for j in range(1,n+1):
    down_star_L = ' ' * (j) + '*' * (2*(n-j)-1)
    down_star_R = (' '*j)+' ' * (j) + '*' * (2*(n-j)-1)
    print(down_star_L,down_star_R,sep='')

