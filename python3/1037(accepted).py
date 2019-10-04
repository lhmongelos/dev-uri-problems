############################################################
### Celso "Shaggy" Antonio - Nov 2017
############################################################

n = float(input())
if(n >= 0):
	if(n <= 100):
		if(n <= 25):
			print('Intervalo [0,25]')
		else:
			if(n <= 50):
				print('Intervalo (25,50]')
			else:
				if(n <= 75):
					print('Intervalo (50,75]')
				else:
					print('Intervalo (75,100]')
	else:
		print('Fora de intervalo')
else:
	print('Fora de intervalo')