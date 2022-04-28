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



#EXERCISE: PAINT AREA CALCULATOR
# You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)