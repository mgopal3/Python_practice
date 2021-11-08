import random
#Hangman Project

#					flowchart
#  					---------
#					1. pick a random word
#					2. generate as many blanks as letter
#					3. ask the user to guess a letter
#					4. check if the letter is in the word
#						if yes: populate the blank 
#								check if the user guessed the word
#								if yes: End of Game (Game Won)
#								if not: check if the user has more turns
#										if yes: jump to step 3
#										if no: End of Game. jump to end (Game Lost)
#						if no: populate the hangman
#							   check if the user has more turns left
#							   if yes: jump to step 3
#							   if no: End of Game. jump to end (Game Lost)
#						End of Game. Display if user lost or Won.

#---------------------------------------Step 1----------------------------------------------#
word_list = ["aardvark", "baboon", "camel"]


#Todo1: Randomly choose a word from the word_list and 
#assign it to a variable called chosen_word
word = random.choice(word_list)
length = len(word)
#print (f"word is {word} and len is {length}")

#Todo2: Ask the user to guess a letter and assign their answer to a variable called guess. 
#Make guess lowercase
guess = input("Guess a letter: ").lower()
if len(guess) > 1:
	printf("incorrect input. Guess a single letter")

#print(f"Your guess is {guess}")


#Todo3: Check if the letter the user guessed (guess) is one of the letter in the chosen_word
for ch in word:
	if guess == ch:
		print("Right")
	else:
		print("Wrong")
#---------------------------------------End of Step 1---------------------------------------#


#---------------------------------------Step 2----------------------------------------------#
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#TODO1: - Create an empty List called 'display'
#For each letter in the chosen_word, add a "_" to 'display'
#So if the chosen_word was apple, display should be ["_","_","_","_","_"]
# with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word: # or for _ in range(len(chosen_word)) goes from [0 to l-1]
	#display.append("_") or
	display += "_"

#print (display)

guess = input("Guess a letter: ").lower()

#TODO2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position
#e.g. If the user guessed "p" and the chosen_word is 'apple',
#then display should be ["_", "p", "p", "_", "_"].
for pos in range(len(chosen_word)):
	if chosen_word[pos] == guess:
		display[pos] = guess


#TODO3: - Print 'display' amd you should see the guessed letter in the correct position and every other letter replace with "_".
print (display)

#---------------------------------------End of Step 2---------------------------------------#

#---------------------------------------Step 3----------------------------------------------#
import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create Blanks
display = []
for _ in range(word_length):
	display += "_"

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guess all the letters in the chosen_word and 'display' has no more blanks ("_"). The you can tell the user they have won

while "_" in display:
	guess = input("Guess a letter: ").lower()

	#check the guessed letter
	for pos in range(word_length):
		if chosen_word[pos] == guess:
			display[pos] = guess


	#TODO3: - Print 'display' amd you should see the guessed letter in the correct position and every other letter replace with "_".
	print (display)
#---------------------------------------End of Step 3---------------------------------------#


#---------------------------------------Step 4----------------------------------------------#
import random

#stages are arranged in decresing order. Meaning the 6 lives is at the end as expected.
stages = ['''
  +---+
  |   |
  o   |
 /|\  |
 / \  |
 ========
  ''', '''
  +---+
  |   |
  o   |
 /|\  |
 /    |
 ========
  ''', '''
  +---+
  |   |
  o   |
 /|\  |
      |
 ========
  ''', '''
  +---+
  |   |
  o   |
 /|   |
      |
 ========
  ''', '''
  +---+
  |   |
  o   |
  |   |
      |
 ========
  ''', '''
  +---+
  |   |
  o   |
      |
      |
 ========
  ''', '''
  +---+
  |   |
      |
      |
      |
 ========
  ''']
 
end_of_game = False 
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left
#Set lives to 6
lives = 6
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create Blanks
display = []
for _ in range(word_length):
	display += "_"

while not end_of_game:
	guess = input("Guess a letter: ").lower()
	#TODO-2: - If guess is not a letter in the chosen_word, 
	#Then reduce lives by 1
	# if lives goes down to 0 then the game should end and it should print You Lose
	# Also, if the person guessed all the letters in the word, the game should print you win.
	#check the guessed letter
	for pos in range(word_length):
		if chosen_word[pos] == guess:
			display[pos] = guess
			
	if guess not in display:
		lives -= 1

	print (f"{' '.join(display)}")
	
	if not "_" in display:
		print ("You Win!!")
		end_of_game = True
		
	if lives == 0:
		print ("You Lose!!")
		end_of_game = True
		
	#TODO-3: - print the ASCII art from the stages that correspondes to the current number of lives
	print(f"{stages[lives]}")
#---------------------------------------End of Step 4---------------------------------------#

#---------------------------------------Step 5----------------------------------------------#
#Step 5

import random
import hangman_art
import hangman_words

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

logo = hangman_art.logo
stages = hangman_art.stages

print(logo)


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
        	if letter in display:
        		print (f"You guessed {letter}. You already guessed that. Pick another")
        	else:
        		display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print (f"You guessed {guess}. That's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
#---------------------------------------End of Step 5---------------------------------------#



