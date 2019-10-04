############################################################
### Celso "Shaggy" Antonio - Nov 2017
############################################################
import math
 
while True:
    try:
        numbers = list(map(int,input().split()))
        a = math.sqrt(144 + numbers[0] * numbers[0])
        tf = 12000.0 / numbers[1]
        tg = (a * 1000) / numbers[2]
        if(tg <= tf):
            print('S')
        else:
            print('N')
    except (EOFError):
        break