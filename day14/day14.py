""" Game called Higher Lower, where we decide who has higher followers on Instagram
"""
from art import logo, vs
from game_data import data
from os import system
from random import randint


system('clear')

num_of_data_elements = len(data)
current_score = 0
#pick a random data value from data
data_item_num_A = randint(0, num_of_data_elements-1)
play = True

while play:
	#display higher lower
	print(f"{logo}\n")
	
	#display A
	data_item_A = data[data_item_num_A]
	print(f"Compare A: {data_item_A['name']}, {data_item_A['description']} from {data_item_A['country']}\n")

	#display vs
	print(f"{vs}\n")

	#pick a random data value from data and display as B. Ensure B and A are not the same
	data_item_num_B = randint(0, num_of_data_elements-1)
	while data_item_num_B == data_item_num_A:
		data_item_num_B = randint(0, num_of_data_elements-1)

	data_item_B = data[data_item_num_B]
	print(f"Against B: {data_item_B['name']}, {data_item_B['description']} from {data_item_B['country']}\n")


	
	#get user input A or B
	inp = input("Who has more followers? Type 'A' or 'B' ")

	#copy followers for A and B
	followers_A = data_item_A['follower_count']
	followers_B = data_item_B['follower_count']

	if followers_A > followers_B:
		ans = 'A'
	else:
		ans = 'B'
		
	system('clear')
	#verify user input to be correct or false
	if ans == inp:
		current_score += 1
		print(f"You're right! Current Score: {current_score}")
		data_item_num_A = data_item_num_B
	else:
		play = False
		print(f"The answer is wrong! Your score is {current_score}")




