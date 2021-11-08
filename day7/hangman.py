import random

#import variables from the other files
from hangman_words import word_list
from hangman_art import stages, logo

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

print(logo)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #check if letter is valid. Also check if letter was previously guessed
        if letter == guess:
        	if letter in display:
        		print (f"You guessed {letter}. You already guessed that. Pick another")
        	else:
        		display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print (f"You guessed {guess}. That's not in the word. You lose a life.")
    	#decrese lives
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
        
	#display the stage of the game the user is in
    print(stages[lives])
