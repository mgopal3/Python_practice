#Scope and Number Guessing Game

############################################# Scope #######################################

enemies = 1 # new variable with global scope

def increase_enemies():
	enemies = 2 # local and new vairable. Entirely diff from above.
	print(f"enemies inside the function: {enemies}") # this is 2

increase_enemies()
print(f"enemies outside the function: {enemies}") # this is 1


#Local scope 
def drink_potion():
	potion_strength = 2
	print(potion_strength)

drink_potion()
#print(potion_strength) # not valid as I can use the variable potion_strength only inside the function


#global scope
player_health = 10 # global

def drink_potion():
	potion_strength = 2
	print(player_health) #global available everywehre
	
print(player_health) #global available everywehre


#when you firt time give name to a function or a variable you have to be aware of where the variables are created. Need to understand the scope

#Does Python have BLock Scope?? NOooo
game_level = 3
enemies = ["Skeletons", "Zombie", "Alien"]
if game_level < 5:
	new_enemy = enemies[0]

print(new_enemy) # this works when used with an if/while/for block. Meaning variables created within the if block can be accessed outside the block, within its scope. if/while/for don't count as creating a local scope

enemies = 1 # new variable with global scope

def increase_enemies():
	global enemies #ensures we use the global value. This is how we tell them to modify the global within a func. Else will return an error.
	enemies += 2 
	print(f"enemies inside the function: {enemies}") # this is 2

increase_enemies()
print(f"enemies outside the function: {enemies}") # this is 1

#avoid modifying global scope within a local scope. This is bad programming

#good practice which doesnt locally modify a gloabla

def increament_enemies():
	return enemies + 1 # here, we read the global variable and return a +1
	
print(increament_enemies())

#global constants

#defined globally but just never modified.

PI = 3.14159 #change to upper case and don't modify

import random
from os import system
from art import logo
#----------------------------------Practice Final ----------------------------------------------#
#Number Guessing Gameeasy
#Instructions:
#

print ("---Practice Final----------------------------------------------")
def number_guessing_game(inp, num_attempts):
	while num_attempts > 0:
		print(f"You have {num_attempts} attempts remaining to guess the number.")
		num_attempts -= 1
		guess = int(input("Make a guess: "))
		if guess == inp:
			print(f"You got it! The answer was {inp}")
			return
		elif guess > inp:
			print(f"Too High.\nGuess Again.")
		elif guess < inp:
			print(f"Too Low.\nGuess Again.")
			
	print("You've run out of guesses, you Lose!")
	return	


system("clear")
print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(0,100)
print(f"Psst! Number is {number}")
hardOrEasy = input("Choose a difficulty. Type 'easy' or 'hard': ")

if hardOrEasy == "easy":
	attempts = 10
elif hardOrEasy	== "hard":
	attempts = 5
else:
	print("Incorrect input, sorry shutting down!")

number_guessing_game(number, attempts)
print ("---End of practice---------------------------------------\n")  
#----------------------------------End of Practice Final---------------------------------------#
