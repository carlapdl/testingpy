#Day 1: 30 Days of python programming
#primitive data types
name = "Carla"
age = 29
height = 5.01
is_student = False

#non-primitive data types
fruits = ["apple", "banana", "mango"]
coordinates = (3, 7)
person = {"name": "Natsu", "age": 25, "is_student": True}

#arithmetic operators
num1 = 10
num2 = 3
add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2
mod_result = num1 % num2
exp_result = num1 ** num2

#comparison operators / logical operator (and)
is_adult = age >= 18
is_teenager = age >=13 and age < 18

count = 0

#functions
def hello():
    print("*** hello() ***")
    print("HELLO WORLD PYTHON!")

def check_age(my_age):
    print("*** check_age() ***")
    print("Given Age: ",my_age)

    if my_age < 18:
        print("You're a minor!")
    elif my_age >= 18 and my_age <= 21:
        print("You're an adult, but not yet allowed to drink liquor!")
    else:
        print("Okay! Go and buy a red wine!") 

def euclidean():
    print("*** euclidean() ***")
    #(2, 3) and (10, 8)
    x1 = 2
    y1 = 3
    x2 = 10
    y2 = 8

    d1 = x2 - x1
    d2 = y2 - y1

    exp1 = d1 ** 2 #exponent 2
    exp2 = d2 ** 2 #exponent 2

    total = exp1 + exp2

    eucl = total ** 0.5 #get the square root

    print("Euclidean distance: ",eucl)

#hello world sample
#print("HELLO WORLD PYTHON!")

#function call to hello()
#hello()

#primitive data types
"""
print("*** Primitive Data Types ***")
print("Name: ",name)
print("Age: ",age)
print("Height: ",height)
print("Student?: ",is_student)
"""

#non-primitive data types
"""
print("*** Non-primitive Data types ***")
print("List: ",fruits)
print("Tuple: ",coordinates)
print("Dictionary: ",person)
"""

#check data types
"""
print("*** Checking Data types ***")
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
"""

#arithmetic operators
"""
print("*** Arithmetic Operators ***")
print("Given numbers: ",num1, ",",num2)
print("Here are the results . . .")
print("Addition: ", add_result)
print("Subtraction: ",sub_result)
print("Multiplication: ", mul_result)
print("Division: ", div_result)
print("Modulus: ",mod_result)
print("Exponentiation: ",exp_result)
"""

#comparison operators
"""
print("*** Comparision Operators ***")
print("Given Age: ",age)
print("Adult?: ",is_adult)
print("Teenager?: ",is_teenager)
"""

#if-else statement
"""
print("*** If-Else Statement ***")
print("Given Age: ",age)
if age < 18:
    print("You're a minor!")
elif age >= 18 and age <= 21:
    print("You're an adult, but not yet allowed to drink liquor!")
else:
    print("Okay! Go and buy a red wine!") 
"""

#function call to check_age()
#check_age(age)

#for loop
"""
print("*** For Loop ***")
for fruit in fruits:
    print(fruit)
"""

#while loop
"""
print("*** While Loop ***")
print("Start count: ",count)
while count < 6:
    print(count)
    count += 1
"""

#break statement
"""
print("*** Break Statement ***")
for i in range(5):
    if i == 3:
        print("Break at i=",i)
        break
    print(i)
"""

#continue statement
"""
print("*** Continue Statement ***")
for i in range(5):
    if i == 2:
        print("Skipped at i=",i)
        continue
    print(i)
"""

#euclidean distance
euclidean()