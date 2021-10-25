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

#find a length of the list
list = [10, 20, 30, 40, 60]
print (f"length of list is: {len(list)}")

#remember to always access elements of the list as 0 to len-1

#nested lists: lists within lists
fruits = ["apple", "orange", "peach", "pear"]
vegetables = ["potato", "tomato", "onion", "ladysfinger", "Beans"]
food = [fruits, vegetables]
print(f"length of fruits: {len(fruits)}")
print(f"length of vegetables: {len(vegetables)}")
print(f"length of food: {len(food)}")

#prints the 2 lists
print(food)

#prints list of fruits
print(food[0])

#prints list of vegetables
print(food[1])

#print individual elements of the list
print(food[0][1])



#Treasure Map Exercise
#given a 3x3 matrix, get user input to place the treasure at a particular location
print ("---Practice 4.3----------------------------------------------")
row1 = [":)", ":(", ":p"]
row2 = [":o", ";p", ":D"]
row3 = [":$", ":#", ":@"]
print(f"{row1}\n{row2}\n{row3}")

matrix = [row1, row2, row3]
#input is in the form of row and coloumn

#inp = int(input("Where do you want to put the treasure? "))
#col = int(inp % 10)
#row = int(inp/10)

#also do the following to make it easier
inp = input("Where do you want to put the treasure? ")
col = int(inp[0])
row = int(inp[1])
if(col > 3 or row > 3):
	print("Incorrect input, No change will be made") 
else:
	matrix[row-1][col-1] = "X"

print(f"{row1}\n{row2}\n{row3}")
print ("---End of practice---------------------------------------\n")   


