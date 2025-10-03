import math

n = int(input('n? '))
summa = 0 
k = 1 
while k <= n:
    summa = summa + k #öka summan med k
    k = k + 1 #öka k med med 1
    print('summan blir', summa)
    if k != n:
        print('summa')
        print('k är nu', k)
print('slutgiltiga summan är', summa)
print('slutgiltiga k är', k)
print('slutgiltiga k är', k)       
