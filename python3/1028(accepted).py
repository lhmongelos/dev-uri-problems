############################################################
### Celso "Shaggy" Antonio - Nov 2017
############################################################

def gdc(x,y):
    while(y != 0):
        z = y
        y = x % z
        x = z
    return x
 
n = int(input())
for i in range(n):
    numbers = list(map(int, input().split()))
    res = gdc(numbers[0], numbers[1])
    print(res)