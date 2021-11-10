#Dictionaries and Nesting

#Dictionaries in Python. Group together and link common information. HOlds key and value pair
#{key:value} eg. {"Bug": "A defect"}
#to have more than one entry. {key1:value1, key2:value2, key3:value3}

#example
programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.", 
	"Function": "A piece of code that you can easily call over and over again."
}
#to retrieve an item from the dictionary
bug = programming_dictionary["Bug"]
print(bug)

#Adding a new entry into the dictinary or reassigning works with the same symtax
programming_dictionary["Loop"] = "The action of doing something over and over agian"

print(len(programming_dictionary))

#Loop thru a dictinary
print("Looping thru the dictionary")
for key in programming_dictionary:
	print(f'key:{key} and value:{programming_dictionary[key]}')
	
#empty dictionary
empty_dictionary = {}

#Wipe the entire dictionary
programming_dictionary = empty_dictionary

print(len(programming_dictionary))


#----------------------------------Practice 9.1----------------------------------------------#

#Grading Programming Exercise
#Instructions:
	#You have access to a databse of scores. Write a program to convert it to grades
	#Scores 91 - 100: Grade = "Outstanding"

    #Scores 81 - 90: Grade = "Exceeds Expectations"

    #Scores 71 - 80: Grade = "Acceptable"

    #Scores 70 or lower: Grade = "Fail"
print ("---Practice 9.1----------------------------------------------")
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
	score = student_scores[student]
	if score > 90:
		student_grades[student] = "Outstanding"
	elif score > 80:
		student_grades[student] = "Exceeds Expectation" 
	elif score > 70:
		student_grades[student] = "Acceptable"
	else:
		student_grades[student] = "Fail"  

# 🚨 Don't change the code below 👇
print(student_grades)
print ("---End of practice---------------------------------------\n")  
#----------------------------------End of Practice 9.1---------------------------------------#

#Nesting 
	#having a one inside the other

nested_dictionary = {
	10: [9,8,7,6,5,4,3,2,1],
	"France": "Paris",
	"travel": ["Paris", "Germany"],
}

#nesting dictionary in a dictionary
travel_log = {
	"france": {
				"cities_visited": ["Paris", "Lille", "Dijon"], 
				"total_cities" : 5, 
				"days_stayed": 15
			  },
	"Germany": {
				"cities_visited": ["Berlin","Koln", "Nuremberg"], 
				"total_cities": 15, 
				"days_stayed": 365
				}
	
}


#nesting multiple dictionaries inside a list
#list are ordered and the items are accessed by their position.
#dictinaries are not ordered and the otems are accessed by their key.

#Each item of the list is a dictionary with multiple key value pairs embedded in them
travel_log = [
	{
		"country":"France", 
		"cities_visited": ["Paris", "Lille", "Dijon"], 
		"total_cities" : 5, 
		"days_stayed": 15	
	},
	{
		"country":"Germany",
		"cities_visited": ["Berlin","Koln", "Nuremberg"], 
		"total_cities": 15, 
		"days_stayed": 365
	},
]


#----------------------------------Practice 9.2----------------------------------------------#
#Dictinary in Lists Exercise
#Instructions:
	#Write a function to add a new Trave_log entry
	
print ("---Practice 9.2----------------------------------------------")
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, visits, list_of_cities):
	new_entry = {}
	new_entry["country"] = country
	new_entry["visits"] = visits
	new_entry["cities"] = list_of_cities
	travel_log.append(new_entry)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
print ("---End of practice---------------------------------------\n")  
#----------------------------------End of Practice 9.2---------------------------------------#

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





