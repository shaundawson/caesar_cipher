#DAY8: Functions with inputs

# #Simple Function
# def greet():
#     print("Hello Shaun")
#     print(f"How do you do Shaun?")
#     print("Isn't the weather nice today?")
# greet()

# #Functions with input
# def greet_with_name(name):
#     print(f"Hello {name} ")
#     print(f"How do you do {name}?")

# greet_with_name("George")

# #Function with more than one input
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}?")

# #Call function with positional argument
# # greet_with("Shaun", "Florida")
    
# #Call funtion with a keyword argument
# greet_with(location="Florida", name = "Shaun")



# #EXERCISE: PAINT AREA CALCULATOR
# # You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy. area = width * height

# import math

# def paint_calc(height, width, cover):
#     number_of_cans = math.ceil((height * width) / cover)
#     print(f"You'll need {number_of_cans} cans of paint")

# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)


#EXERCISE: PRIME NUMBER CHECKER
#Prime numbers are numbers that can only be cleanly divided by themselves and 1.  Write a function that checks whether the number passed into it is a prime number or not.

# def prime_checker(number):
#     if number > 1:
#     # Iterate from 2 to n / 2
#         for i in range(2, int(number/2)+1): 
#             # If num is divisible by any number between
#             # 2 and n / 2, it is not prime
#             if (number % i) == 0:
#                 print(f"{number} is not a prime number")
#                 break
#         else:
#             print(f"{number} is a prime number")
  
#     else:
#         print(f"{number} is not a prime number")

# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print(f"{number} is a prime number")
#     else: 
#         print(f"{number} is not a prime number")    

# n = int(input("Check this number: "))
# prime_checker(number=n)


# Exercise - Caesar Cipher
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
        

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_amount = shift)
else:
    decrypt(cipher_text=text, shift_amount = shift)