############################################################
### Celso "Shaggy" Antonio - Nov 2017
############################################################

def isPrime(x):
    if(x == 1):
        return 0
    if(x == 2):
        return 1
    if(x % 2 == 0):
        return 0
    num = 3
    while(num * num <= x):
        if(x % num == 0):
            return 0
        num += 2
    return 1
 
n = int(input())
for i in range(n):
    y = int(input())
    if(isPrime(y)):
        print('Prime')
    else:
        print('Not Prime')