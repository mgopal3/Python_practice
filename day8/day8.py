# functions with Inputs. Arguments and Parameters. ceaser cipher

#funtion: handy way to package a bunch of code together

#A simple function 
def greet():
	print("hello!")
	print("I still remeber how a function works")
	print("This is my line 3. Very creative")


#to add somthing to the paranthesis
#def myfunc(something):
	#do something with something

def greet_with_name(name):
	print(f"hello {name}!")
	print(f"I still remeber you {name}")
	print("This is my line 3. Very creative")
	
#greet_with_name("My3")

#Functions with more than one input
def greet_with_name_and_location(name, location): 
	print(f"Hio {name} from {location}")
	print(f"Welcome to {location}")

#greet_with_name_and_location("My3", "Bangalore") #positional arguments


greet_with_name_and_location(name="My3", location="Bangalore") #keyword argument. Can switch around the arguments in this form.

#or 

greet_with_name_and_location(location="Bangalore", name="My3")


print ("---Practice 8.1----------------------------------------------")
#PROBLEM
#Paint Area Calculator
#You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.
#number of cans = (wall height ✖️ wall width) ÷ coverage per can.
#e.g. Height = 2, Width = 4, Coverage = 5
#number of cans = (2 ✖️ 4) ÷ 5
#                    = 1.6
#But because you can't buy 0.6 of a can of paint, the result should be rounded up to 2 cans.

#SOLUTION
#Write your code below this line 👇
import math # going to use this to find the ceil function or to round up
def paint_calc(height, width, cover):

	number_of_cans = height*width/cover
	print(f"={math.ceil(number_of_cans)}")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
print ("---End of practice 8.1---------------------------------------\n") 

print ("---Practice 8.2----------------------------------------------")
#PROBLEM
#Prime Number Calculator
#Prime numbers are numbers that can only be cleanly divided by itself and 1.
#You need to write a function that checks whether if the number passed into it is a prime number or not.
#e.g. 2 is a prime number because it's only divisible by 1 and 2.
#But 4 is not a prime number because you can divide it by 1, 2 or 4.

#Write your code below this line 👇

def prime_checker(number):
	is_prime = True
	for n in range(2,number):
		if number%n == 0:
			is_prime = False
			#print(f"{number} is not a prime number.")
			return
	if is_prime is True:
		print(f"{number} is a prime number")
	



#Write your code above this line 👆
    
#Do NOT change any of the code below👇
#n = int(input("Check this number: "))
for n in range(101):
	prime_checker(number=n)
print ("---End of practice 8.2---------------------------------------\n")  

print ("---Practice 8.3----------------------------------------------") 
#Ceaser Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


def encrypt(text, shift) :
	alphabet_len = len(alphabet)

	cipherText = ""

	for ch in text:
		idx = alphabet.index(ch)
		idx = (idx+shift)%alphabet_len
		cipherText += alphabet[idx]
		
	print ((f"The cipher text is : {cipherText}"))		
		
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

encrypt(text, shift)
print ("---End of practice 8.3---------------------------------------\n") 

print ("---Practice 8.4----------------------------------------------") 
#Ceaser Cipher part 2. Decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(plain_text, shift_amount) :
	alphabet_len = len(alphabet)

	cipherText = ""

	for ch in plain_text:
		idx = alphabet.index(ch)
		idx = (idx+shift_amount)%alphabet_len
		cipherText += alphabet[idx]
		
	print ((f"The cipher text is : {cipherText}"))		
		
#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"

def decrypt(cipher_text, shift_amount) :
	alphabet_len = len(alphabet)
	plain_text = ""
	
	for ch in cipher_text:
		idx = alphabet.index(ch)
		idx = (idx - shift_amount)%alphabet_len
		plain_text += alphabet[idx]
		
	print(f"The plain text is: {plain_text}")
	
#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.


if direction == "encode":
	encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
	decrypt(cipher_text=text, shift_amount=shift)
else:
	print("Incorrect option picked!")
	
print ("---End of practice 8.4---------------------------------------\n")  

print ("---Practice 8.5----------------------------------------------") 
#Ceaser Cipher part 3. Make Encryption and Decryption pretty. 
#Create one function based on the direction
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser (inp_text, shift_amount, direction) :
	alphabet_len = len(alphabet)
	result = ""
	if direction == "decode":
		shift_amount *= -1
			
	for ch in inp_text:
		idx = alphabet.index(ch)
		idx = (idx+shift_amount)%alphabet_len
		result += alphabet[idx]
		
	print ((f"The {direction}d text is : {result}"))
	
ceaser(inp_text=text, shift_amount=shift, direction=direction)	
print ("---End of practice 8.5---------------------------------------\n")  

import art

print ("---Practice 8.6----------------------------------------------") 
print (art.logo)
#Ceaser Cipher part 4. Add a pretty heading and be able to include strings in the input 
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def ceaser (inp_text, shift_amount, direction) :
	alphabet_len = len(alphabet)
	result = ""
	if direction == "decode":
		shift_amount *= -1
			
	for ch in inp_text:
		if not ch in alphabet:
			result += ch
		else:
			idx = alphabet.index(ch)
			idx = (idx+shift_amount)%alphabet_len
			result += alphabet[idx]
		
	print ((f"The {direction}d text is : {result}"))


keep_going = True
while keep_going :

	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	ceaser(inp_text=text, shift_amount=shift, direction=direction)	
	
	if input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower() == "no":
		keep_going = False
		print("Good Bye! ")
			
print ("---End of practice 8.6---------------------------------------\n")  

