#day1: print statement | string manipulation | input data | variables
#remember indentation matters a lot :( 
#python also acts as an intepretor and only gives you one error at a time :( 

print ("I remember how to print text and use the print character\n") # the double quotes is used for text
print ("---Practice----------------------------------------------")
print ("Day 1 - Python Print Function")
print ("The function is declarewd like this")
print ("print('what to print')") #notice I've used single quote cause the double quote is outside
print ("---End of practice---------------------------------------\n")

#the next 2 statements work the same way
print ("print(\"what to print\")")
print ('print("what to print")')


#string and string manipulation
print ("Hello world\nHello world")

#string concatination
print ("hello " + "2nd part of the string\n")

print ("---Practice----------------------------------------------")
print ("Day 1 - String Manipulation")
print ("String Concatination is done with the \"+\" sign")
print ("e.g. print(\"Hello\" + \"world\")")
print ("New  lines can be created with a backslash and n")
print ("---End of practice---------------------------------------\n")

#input functions 
input("A prompt for the user")
input("what is your name?")

#here we are using the input and printint it. In this case first the input is evaluated and then the value is printed as hello <input>
print("Hello " + input("what is your name?")) 

print ("---Practice----------------------------------------------")
#pick input from the user and get the number of characters in the string
print(len(input ("What is your name? ")))
print ("---End of practice---------------------------------------\n")

#python variable
name = input("what is your name? ")
print (name)
#variables can be reassigned with anything
name = 10
print (name)

print ("---Practice----------------------------------------------")
#pick 2 variables and exchange their values
a = input("a = ");
b = input("b = ");

print("a = " + b)
print("b = " + a)

#or

d = a
a = b
b = d

print("a = " + a)
print("b = " + b)

print ("---End of practice---------------------------------------\n")

#Variable naming
#seperate words with _ and don't use number in the begining
#don't use key words

print ("---Final Practice----------------------------------------\n")
#Band Name generator. Input city and pets name and concatinate the 2 for a band name
print ("Welcome to the Band Name Generator\n")
city = input ("What's the name of the city you grew up in?\n")
pet = input ("What's the name of your pet?\n")
band_name = city + " " + pet
print("Your band name could be " + band_name)
print ("---End of practice---------------------------------------\n")


