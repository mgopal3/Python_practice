#blackjack capstone project / 21
#********************************

# we have to get as close to 21 as possible. Over 21 is a direct loss.
# value of cards from 2 to 21 is it's face value. And K,Q n J each is 10.
# A can either be a 1 or a 11
# dealer and person have same card, then it's a draw.
# if dealer has 17 or lesser, he has to get a card

from art import logo
import random
from os import system


cards_dictionary = {
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	"8": 8,
	"9": 9,
	'10': 10,
	"K": 10,
	"Q": 10,
	"J": 10,
	"A": 11
}

card_list = []
for card in cards_dictionary:
	card_list.append(card)

#modifying it to produce a sum close to 21 considering both A as 1 and 11
def sum_of_cards(cards):
	sum_a_1 = 0
	sum_a_11 = 0
	for card in cards:
	    if card == 'A':
	    	sum_a_1 += 1
	    	sum_a_11 += 11
	    else:
	    	sum_a_1 += cards_dictionary[card]
	    	sum_a_11 += cards_dictionary[card]
	#return whatever is closer to 21
	if sum_a_1 > 21 and sum_a_11 > 21 :
		return sum_a_1
	elif sum_a_1 >21:
		return sum_a_11
	elif sum_a_11 > 21:
		return sum_a_1
	else:
		return sum_a_11
	
def calculate_winner(player_total, computer_total):
	if (21 - player_total) < (21 - computer_total):
		print("You Win")
	elif (21- player_total) > (21-computer_total):
		print("Computer Wins")
	else:
		print("It is a draw")
		
def calculate_direct_loss(total):
	if total > 21:
		return True

def game_of_black_jack():
	player_total = 0
	computer_total = 0	
	
#	print(card_list)		
#	for card in card_list:
#		print (f"{cards_dictionary[card]} ")
		
	player_cards = []
	computer_cards = []

 	#pick 2 cards for the player and the computer
	player_cards += random.choice(card_list)
	player_cards += random.choice(card_list)

	computer_cards+= random.choice(card_list)
	computer_cards+= random.choice(card_list)

	#Display the initial cards
	print(f"Your cards : [{player_cards[0]}, {player_cards[1]}]")
	print(f"Computer's first card : {computer_cards[0]}")

	player_wants_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

	if player_wants_another_card == 'y':
		player_cards += random.choice(card_list)
	
	player_total = sum_of_cards(player_cards)
		
	if computer_total < 17:
		computer_cards+= random.choice(card_list)
	
	computer_total = sum_of_cards(computer_cards)
		

	print(f"Your final hand: {player_cards}")
	print(f"Computer's final hand: {computer_cards}")



	if calculate_direct_loss(player_total):
		print("You Lose")
		return
			
	if calculate_direct_loss(computer_total):
		print("Computer Loses")
		return
			
	calculate_winner(player_total, computer_total)	
			
player_wants_to_play = True

while player_wants_to_play:
	system("clear")
	print (logo)
	print()
	game_of_black_jack()
	if input("Do you want to play another game of Blackjack? Type 'y' or 'n': ").lower() == "n":
		player_wants_to_play = False
			
		

