#day4 udemy
#Randomization and Python Lists

#Randomization: python uses the Mersenne Twister to produce pseudo random numbers

#import ramdom python module
import random 

random_integer = random.randint(1, 10) # any integer between 1 and 10 including these
print(f"random number is : {random_integer}")

# any floating point number between 0.00000000... and 0.999999999...
random_float = random.random()
print(f"random floar : {random_float}")

#generate floating point number between 0 and 5
print(f"random float between 1 and 5 : {random_float*5}")

love_score = random.randint(1, 100)
print(f"Your Love Score is {love_score}")

#Heads or Tails
# a random coin generator
print ("---Practice 4.1----------------------------------------------")
coinToss = random.choice(['Head', 'Tail'])
print(f"{coinToss}")

#or

coinToss = random.randint(0,1)
if coinToss == 1:
	print("Heads")
else:
	print("Tails")

print ("---End of practice---------------------------------------\n")    


#python lists

#list is a datastructure. which is a way of roganizing and storing data
# it is a way of storing groups of data

fruits = ["apple", "orange", "Pear"]

#maintains the order of data

#starting from the begining of the list
print(fruits[0])

#start counting from the end of the list
print(fruits[-1])

#to rewrite the item at position 1
fruits[1] = "papaya"

#to add a single item to the end of the list
fruits.append("orange")

vegetables = ["tomato", "onion"]
#to add list at the end of the list
fruits.extend(vegetables)

print(fruits)

import random
#Banker Roulett - Who will pay the bill
#Everybody puts their card in and we randomly pick one to decide who pays. 
#Take names from the user 
print ("---Practice 4.2----------------------------------------------")
names_string = input("Give me everybody's names, seperated by comma: ")
names = names_string.split(", ") #splits the input string by comma and returns a list
number_of_people = len(names)
bill_payer = random.choice(names)
print(f"{bill_payer} pays the bill today")
print ("---End of practice---------------------------------------\n")   

