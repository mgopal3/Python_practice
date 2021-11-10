#----------------------------------Practice Final----------------------------------------------#
#Blind Auction
#Instructions:
	#Write code to save people's name and thier silent auction bid. At the End print the winner of the silent auction
	
from os import system
from art import logo
#HINT: You can call system('clear') to clear the output in the console.

print(logo)
print()
silent_auction = {}
more_auctioners = True

while more_auctioners:
	name = input("What is your name?: " ).lower()
	bid = int(input("What is your bid?: $"))
	silent_auction[name] = bid
	if input("Are there more auctioners (yes/no)? : ").lower() == "no":
		more_auctioners = False
	system("clear")

print(silent_auction)


max = 0
winner = []
for person in silent_auction:
	bid = silent_auction[person]
	if max < bid:
		max = bid
		winner.clear()
		winner.append(person)
	elif max is bid:
		winner.append(person)

print(f"The winners with the max bid of {max} are {winner}")	


#----------------------------------End of Practice Final---------------------------------------#


