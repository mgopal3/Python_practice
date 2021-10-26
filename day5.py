#For Loops, Range and Code Blocks

#For Loops with Python Lists, symtax below
#for item in list_of_items:
	#Do something 

#this simply assigns a variable to each element in the list and does whatever it is supposed to do
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
	print(fruit)
	print (fruit + " Pie")
	
#Average Student Heights rounded to nearest whole number
print ("---Practice 5.1----------------------------------------------")
student_heights = input("Input list of student heights seperated by , : ").split(", ")
for n in range(0, len(student_heights)):
	student_heights[n] = int(student_heights[n])

print (student_heights)

#sum = 0
#for height in student_heights:
#	sum += height

#easier way to find the sum of elements of a list
sum = sum(student_heights)
avg = sum/len(student_heights)

print(round(avg, 0))	
print ("---End of practice---------------------------------------\n")  

#Highest Score
# Write a program to calculate the highest score in a list of scores
# try max and min func but also solve it without
print ("---Practice 5.2----------------------------------------------")

scores = input("student scores: ").split(",")
for n in range(0, len(scores)):
	scores[n] = int(scores[n])

#Use max and min function with lists	
#print(max(scores))
#print(min(scores))

max_score = -1
for score in scores:
	if max_score < score:
		max_score = score
	
	
print(max_score)
print ("---End of practice---------------------------------------\n")  

#for loop and range of numbers

sum = 0
for num in range(1,3): # doesnt include the last number
	sum += num
print (sum)

sum = 0
for num in range(1,11,3): # 1 to 11 with step 3
	sum += num
print (sum)

#find sum of numbers for 1 to 100
sum = 0
for num in range(1,101): # 1 to 101
	sum += num
print (sum)


#Adding Evens Exercise
#Calculate sum of all even numbers from 1 to 100
print ("---Practice 5.3----------------------------------------------")
sum = 0
for n in range(0,101,2):
	sum += n
print(sum)

#second methos of doing it
sum = 0
for n in range(1,101):
	if n % 2 == 0:
		sum += n
print(sum)
print ("---End of practice---------------------------------------\n")  

#FizzBuzz 
#Your program shoud print each number from 1 to 100
#when num is divisible by 3 then instead of the number print "Fizz"
#when num is divisible by 5, then instead of the number print "Buzz"
#if the number is divisible by both 3 and 5 e.g 15, then instead of the number print "FizzBuzz"
print ("---Practice 5.4----------------------------------------------")
for n in range(1, 101):
	if n%3 == 0 and n%5 == 0:
		print ("FizzBuzz")
	elif n%3 == 0:
		print("Fizz")
	elif n%5 == 0:
		print("Buzz")
	else:
		print (n)

#The rest of this is to verify questions in my own head	
l1 = []
l2 = []
for n in range(1, 101):	
	if n%3 == 0 and n%5 == 0:
		l2.append(n)
			
	if n%15 == 0:
		l1.append (n) 

l2.append(10)
print(l1)
print(l2)
if l1 == l2: #seems to compare the lists correctly 
	print("Equal")
print ("---End of practice---------------------------------------\n")  

import random

#PyPassword generator
#generator scrambled random passwords
print ("---Practice Final----------------------------------------------")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
			'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
			'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
			'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print('Welcome to PyPasswordGenrator!')		
num_of_letters = int(input("How many letters would you like in your password? "))
num_of_symbols = int(input("How many symbols would you like in your password? "))
num_of_numbers = int(input("How many numbers would you like in your password? "))

character = []
for i in range(0, num_of_letters):
	character.append(random.choice(letters))

for i in range(0, num_of_symbols):
	character.append(random.choice(symbols))
	
for i in range(0, num_of_numbers):
	character.append(random.choice(numbers))
	
#create a random string out of character list
password = ""

#instead of the above, we can also use the random.shuffle(list) to shuffel the list and convert it to a password
password2 = ""
random.shuffle(character)
for c in character:
	password2 += c
print (f"Here is your password: {password2}")


for i in range(0, len(character)):
	n = random.randint(0, len(character)-1)
	password = password + character[n]
	character.pop(n)

print (f"Here is your password: {password}")
print ("---End of practice---------------------------------------\n")  


