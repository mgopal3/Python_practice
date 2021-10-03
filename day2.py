#day2.py: following the udemy tutorial 
#data-types | Numbers | Operations | Type Conversion | f-Strings | perform a tip calculator

#review the len operator
print ("length of Hello "); print(len("Hello"));

#Data Types

#1. String
#getting a particular charater in a string
print("Hello"[0]) 
print("Hello"[1]) 
print("Hello"[2]) 
print("Hello"[3]) 
print("Hello"[4]) 

#"123" is a string
#concatination of 2 strings that contain numbers
print("123"+"345")

#2. Integer
#adding 2 numbers
print(123+345)

#like in a normal language we use 1,20,346 to write a number, in python we can use 1_20_346
print(1_20_346 + 2_30_456) #this is understood the way hums understand numbers, but it prints the number out normally

#3. Float
print(3.4141)

#4. Bool
print(True)
print(False)

num_char = len(input("What is your name? "))

#This statement results in a type_error
#print("Your name has " + num_char + " characters")
#print(type(num_char)) # prints class 'int'

#print cannot concatinate and integer to a string above

#type casting: to change one type to another
num_char_str = str(num_char) #cast integer to string and print
print("Your name has " + num_char_str + " characters")

#print ("---Practice 2.1 ----------------------------------------------")
#enter a 2 digit number and calculate the sum of the digits
#eg. input: 28 print 10
str_inp = input("Type a 2 digit number: ")
print(type(str_inp[0])) # suprisingly a string
sum_of_digits = int(str_inp[0]) + int(str_inp[1])
print(sum_of_digits)
#print ("---End of practice--------------------------------------------\n")


#mathematical operator
#print(7-3)
#print (3*2)
#print(5/2) # always a floating poin number in python
#print(5**3) #exponent

#PEMDAS - paranthesis, exponents, multiplication, division, addition or subtaction
# multiplicaiton and division have the same priority and whatever is on the left is executed first
print(3*3+3/3-3)  # output is a floating point number #ans is 7.0
print(3*(3+3)/3-3)  # output is a floating point number #ans is 3.0

#print ("---Practice 2.2 ----------------------------------------------")
#BMI calculator based on the weight and height
#bmi is weight(kg)/height in m2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight)/(float(height) ** 2)
print(int(bmi))
print ("---End of practice--------------------------------------------\n")

#manipulation and fstring
print(round(8/3 , 2)) #round to 2 decimal places

print(8 // 3) # floor devision used to chop off all the float and convert to a integer

result = 4 / 2 
result /= 2
print (result)

#other operators are += -= *= /=
score = 0
height = 1.8
isWinning = True

#how to print all this without converting it to string. Use f-string
#fstring automatically converts all the types in {} to a string.
print(f"your score is {score} with height {height} winning {isWinning}")


#print ("---Practice 2.3 ----------------------------------------------")
#calculate the number of days weeks and months
current_age = int (float( input("What is your current age ") )) # need to convert string to a flaot to int for years like 12.5

final_age = 90
left = final_age-current_age #(in years)
print(f"You have {left*365} days, {int(left*52.14)} weeks and {left*12} months left")
print ("---End of practice--------------------------------------------\n")


print ("---Practice Final ----------------------------------------------")
#Tip Calculator
print("Welcome to the tip Calculator")
tot_bill = float(input("What was the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
result = round ( (((tot_bill + (tip_percentage/100) * tot_bill))/num_of_people) , 2)
print(f"Each person should pay: ${result}")

print ("---End of practice--------------------------------------------\n")





