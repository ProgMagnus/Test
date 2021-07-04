import random
import time
import sys
import re

print('Hola! Guess the number\nfrom 1 to 20')

class RunGame():
	game = True
	player_score = 0
	pc_score = 0

def run():
	quantity = 0
	pc_number = random.randint(1, 20)
	while quantity < 6:
		player_number = int(input())
		quantity += 1
		if player_number > 20 and player_number < 99:
			print('I said it was a number between 1 and 20.')
		if player_number > pc_number and player_number < 21:
			time.sleep(0.5)
			print('Your number is greater than mine!')	
		elif player_number < pc_number:
			time.sleep(0.5)
			print('Your number is less than mine')			
		elif player_number == pc_number: 
			break
		elif player_number == 99:
			time.sleep(0.5)
			print('Bye!')
			time.sleep(0.5)
			sys.exit()	
	if player_number == pc_number:
		g.player_score += 1
		time.sleep(0.5)
		print(f"You won!\nResults:\nwin: {g.player_score}, lose: {g.pc_score} \nIf you want to exit type '99'")
	elif player_number != pc_number:
		g.pc_score += 1
		time.sleep(0.5)
		print(f"You lose!\nMy number was: {pc_number}\nResults:\nwin: {g.player_score}, lose: {g.pc_score} \nIf you want to exit type '99'")
		
g = RunGame()
while g.game == True:
	run()
