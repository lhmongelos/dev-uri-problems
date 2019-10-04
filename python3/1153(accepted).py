############################################################
### Celso "Shaggy" Antonio - Nov 2017
############################################################

def long_fatorial(x):
	if(x == 1 or x == 0):
		return 1
	else:
		return x * long_fatorial(x - 1)

print(long_fatorial(int(input())))