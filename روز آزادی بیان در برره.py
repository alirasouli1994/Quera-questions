# روز آزادی بیان در برره
# https://quera.org/problemset/10162/ 

import os
os.system('cls' if os.name == 'nt' else 'clear')

def malison(k):
 
        if k%2!=0:
            return 'Payin Barare'
        else:
            return 'Bala Barare'
    
k=int(input())
print(malison(k))


