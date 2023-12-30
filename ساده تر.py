# ساده تر
# https://quera.org/problemset/3403
a= []
for i in range(4):
    a.append(float(input()))
print("Sum : {:.6f}".format(sum(a)))
print("Average : {:.6f}".format(sum(a)/4))
print("Product : {:.6f}".format(a[0]*a[1]*a[2]*a[3]))
print("MAX : {:.6f}".format(max(a)))
print("MIN : {:.6f}".format(min(a)))
