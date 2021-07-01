import random
import time

print('Hola! find my num\nbetween 1 - 2')

class RunGame():
	game = True

def run():
	qt = 0
	pn = random.randint(1, 20)
	while qt < 6:
		ur = int(input())
		qt += 1
		
		if ur > pn:
			print('ur >')	
		if ur < pn:
			print('ut <')			
		if ur == pn:
			print('win') 
			break	
	if ur != pn:
		print('u lose')
		
g = RunGame()
while g.game == True:
	run()