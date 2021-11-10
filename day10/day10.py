#Continuing functions. Functions with Outputs

#def my_func(parameter1):
	#do something
	#return something
#output = my_func(argument1)

#examples
#takes the first and last name and converts it to title case
def format_name(f_name, l_name):
	if f_name == "" or l_name == "":
		return
	#full_name = (f_name + " " + l_name).title()
	#return full_name
	
	#or below
	#formatted_f_name = f_name.title()
	#formatter_l_name = l_name.title()
	#return f"{formatted_f_name} {formatter_l_name}" #f is to format string
	
	#or as below
	return (f_name + " " + l_name).title()
	
	
full_name = format_name("aBcD", "EfGh")
print(full_name)
full_name = format_name("", "")
print(f"what is the full name here: {full_name}")

#----------------------------------Practice 10.1 ----------------------------------------------#
#Days in a month
#Instructions:
	#You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.
	
print ("---Practice 10.1----------------------------------------------")
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if month < 0 or month > 12:
  	return "Invalid Month"
  if month == 2 and is_leap(year):
  	return month_days[month-1] + 1
  	
  return month_days[month - 1]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

print ("---End of practice---------------------------------------\n")  
#----------------------------------End of Practice 10.1---------------------------------------#


#doc strings. Create a little documents for every func so it shows up when u use it.
def format_name(f_name, l_name):
	"""Take a first and last name and format it to 
	return the title case version of the name"""
	return
	
	
#----------------------------------Practice Final ----------------------------------------------#
#Calculator
#Instructions:
	#Program a calculator

print ("---Practice Final----------------------------------------------")

from art import logo
from os import system

system('clear')
print (logo)
print()

def calculator(num1, num2, operation):
	""" performs + - * / % operations 
		Enter 2 numbers and a valid operation as a string
	"""
	if operation == '+':
		return num1+num2
	elif operation == '-':
		return num1 - num2
	elif operation == '*':
		return num1 * num2
	elif operation == '/':
		if num1 != 0:
			return num1/num2
		else:
			return "divide by 0 exception"
	elif operation == '%':
		return num1 % num2
	else:
		return "Incorrect operation specified"
		
continue_calculation = True
num1 = int(input("What's the first number?: "))
print(f'+\n-\n\\\n*\%')

while continue_calculation:
	operation = input("Pick an operation: ")
	num2 = int(input("What's the next number?: "))
	result = calculator(num1, num2, operation)
	print(f"{num1} {operation} {num2} = {result} ")
	inp = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
	if inp == 'n':
		continue_calculation = False
	num1 = result
		
print ("---End of practice---------------------------------------\n")  
#----------------------------------End of Practice Final---------------------------------------#



#----------------------------------Practice Final ----------------------------------------------#
#Calculator
#Instructions:
	#Program a calculator using a dictionary

print ("---Practice Final----------------------------------------------")

from art import logo
from os import system

system('clear')
print (logo)
print()

def add(a, b):
	return a+b

def subtract(a,b):
	return a-b
	
def multiply(a,b):
	return a*b

def divide(a,b):
	if b == 0:
		return "Invalid Input"
	return a/b

def modulo(a,b):
	return a%b

operations = {
	'+' : add,
	'-'	: subtract,
	'*' : multiply,
	'/' : divide,
	'%' : modulo
}


		
continue_calculation = True
num1 = float(input("What's the first number?: "))

for op in operations:
	print (op)

while continue_calculation:
	op = input("Pick an operation: ")
	num2 = float(input("What's the next number?: "))
	func = operations[op]
	result = func(num1, num2)
	print(f"{num1} {op} {num2} = {result} ")
	if(result == "Invalid Input"):
		continue_calculation = False
	
	else :
		inp = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
		if inp == 'n':
			continue_calculation = False
		num1 = result
		
print ("---End of practice---------------------------------------\n")  
#----------------------------------End of Practice Final---------------------------------------#



