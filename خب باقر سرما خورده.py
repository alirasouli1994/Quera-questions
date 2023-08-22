a = []
for i in range(1,6):
    b =input()
    if 'MOLANA' in b or 'HAFEZ' in b :
        a.append(i)
if len(a) > 0 :
    print(' '.join(map(str, a)))
else :
    print('NOT FOUND!')
