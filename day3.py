#day3 udemy
#Conditional Statements | Logical Operators | Code Blocks & Scope

#1. Conditional if and else

# if condition:
#	do this
#else:
#	do this

#indentation in the if statement is super important

#Roller Coaster Problem
print ("---Practice----------------------------------------------")
print ("Welcome to the rollercoaster")
height = int(input("what is your height in cms? "))
if height > 120:
	print("You can ride the rollercoaster!")
else:
	print("You cannot ride the roller coaster!")

print ("---End of practice---------------------------------------\n")


#operators: > < >= == <= 

#Check if a number is even or odd
print ("---Practice 3.1--------------------------------------------")

number = int(input("Which number do you want to check? "))
if number%2 == 0:
	print("This is an Even Number")
else:
	print("This is an Odd Number")

print ("---End of practice---------------------------------------\n")


#Nested if and Else statements

#if condition:
#	if another condition:
#		do this
#	else:
#		do this
#else:
#	do this	
	
#Roller coaster Ride with a payment check
#height >120 cm && if age>18 cost is $12 else $7
#Roller Coaster Problem
print ("---Practice----------------------------------------------")
print("Welcome to the Roller Coaster Part 2")
height = int(input("what is your height in cms? "))
age = int(input("what is your age? "))

if height > 120:
	if age < 12:
		print("Please pay $5")
	elif age <=18:
	 	print("Please pay $7")
	else:
		print("Please pay $12") 
else:
	print("You cannot ride the roller coaster!")
	
print ("---End of practice---------------------------------------\n")


#BMI 2.0 - Also tells you if you are underweightor normal weight or overweight or obese or clinically obese
print ("---Practice 3.2--------------------------------------------")


height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight/height**2, 1)

if bmi < 18.5:
	print(f"your bmi is {bmi} and you are underweight")
elif bmi < 25:
	print(f"your bmi is {bmi} and you are normal weight")
elif bmi < 30:
	print(f"your bmi is {bmi} and you are overweight")
elif bmi < 35:
	print(f"your bmi is {bmi} and you are obese")
else:
	print(f"your bmi is {bmi} and you are clinically obese")

print ("---End of practice---------------------------------------\n")



#Leap year challenge
#is a leap year if evenly divisible by 4 except evenly divisible by 100 unless the year is als evenly divisible by 400
print ("---Practice 3.3--------------------------------------------")
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
	if year % 100 != 0:
		print ("It is a leap year")
	elif year % 400 == 0:
		print("It is a leap year")
	else:
		print("It is not a leap year")
else:
	print("It is not a leap year")

print ("---End of practice---------------------------------------\n")

#Multiple if statements in  succession
#if condition:
#	do A1
#if condition2:
#	do A2

#Roller coaster Ride with a payment check & check for if they need a photo
#height >120 cm && if age>18 cost is $12 else $7
#Roller Coaster Problem
print ("---Practice----------------------------------------------")
print("Welcome to the Roller Coaster Part #3")
height = int(input("what is your height in cms? "))
age = int(input("what is your age? "))
need_photo = input("Do you want a photo(y/n)? ")
cost  = 0
if height > 120:
	if age < 12:
		cost = 5
	elif age <=18:
	 	cost = 7
	else:
		cost = 12
else:
	cost = 0
	
if cost > 0:
	if need_photo == "y":
		print(f"Please pay ${cost+3}")
	else:
		print(f"Please pay ${cost}")
else:
	print("You cannot ride the roller coaster!")
	
print ("---End of practice---------------------------------------\n")                                  

#Calculate the cost of pizza
# S = 15 / M = 20 / L = 25
# pepperoni for small is +2
# perpperoni for medium or large = +3
# Extra cheese for any pizza is +1
print ("---Practice 3.4 ----------------------------------------------")
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S,M,L? ")
add_pepperoni = input("Do you want pepperoni? y/n? ")
extra_cheese = input("Do you want Extra Cheese? y/n? ")

bill = 0
if size == "S":
	bill += 15
elif size == "M":
	bill += 20
elif size == "L":
	bill += 25

if add_pepperoni == "y":
	if size == "S":
		bill += 2
	else:
		bill += 3

if extra_cheese == "y":
	bill += 1

print(f"Your bill today is ${bill}")
print ("---End of practice---------------------------------------\n")   


#Logical operators
# A and B / A or B / not A

#Roller coaster Ride with a payment check & check for if they need a photo
#height >120 cm && if age>18 cost is $12 else $7
# Free tickets to anybody between the age of 45 & 55
#Roller Coaster Problem with a mid life crises
print ("---Practice----------------------------------------------")
print("Welcome to the Roller Coaster Part #4")
height = int(input("what is your height in cms? "))
age = int(input("what is your age? "))
need_photo = input("Do you want a photo(y/n)? ")
cost  = 0
if height > 120:
	if age < 12:
		cost = 5
	elif age <=18:
	 	cost = 7
	else: 
		cost = 12
else:
	cost = 0
	
if cost > 0:
	if age >=45 and age <= 55:
		print("You ride free! ")
	elif need_photo == "y":
		print(f"Please pay ${cost+3}")
	else:
		print(f"Please pay ${cost}")		
else:
	print("You cannot ride the roller coaster!")
	
print ("---End of practice---------------------------------------\n")  

# Love Calculator
#calculate the number of time true love occurs in your names and concatinate the answer
#we learn to use .count() to get number of times a charater occured in a string and 
#.lower() to move all the characters to the lower case
print ("---Practice 3.5 ----------------------------------------------")
print("Welcome to the love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name = (name1 + name2).lower()
true_count = 0
love_count = 0
true_count += name.count("t")
true_count += name.count("r")
true_count += name.count("u")
true_count += name.count("e")

love_count += name.count("l")
love_count += name.count("o")
love_count += name.count("v")
love_count += name.count("e")

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
	print(f"Your score is {score}, you go together like coke and mentos")
elif score >= 40 and score <= 50:
	print(f"Your score is {score}, you are alright together")
else:
	print(f"Your score is {score}")

print ("---End of practice---------------------------------------\n")    

#treasure island game
print ("---Practice Final ----------------------------------------------")
print("Welcome to the Treasure Island Game! Your mission is to find the treasure.")
inp = input("You are at your favorite ice cream shop, do you wanna go left or right? ").lower()
if inp == "left":
	inp = input("You walked far enuf and got to a lake, do you now wanna swim or wait ").lower()
	if inp == "wait":
		inp = input("You made the right choice. I give you 3 doors red/yellow/blue. Which do you pick? ").lower()
		if inp == "yellow":
			print("Congratulations! You Won!")
		else:
			print("Sorry, This door has a crocodile behind it. You Lose. Game Over!")
	else:
		print("Sorry, too dangerous to swim here. You are dead. Game Over!")	
else:
	print("Sorry, No ice cream for you. Game Over!")
print ("---End of practice---------------------------------------\n")   





















