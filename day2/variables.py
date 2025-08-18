#Day 2: 30 Days of python programming

#Exercise Level 1
first_name = "Natsu"
last_name = "Dragneel"
full_name = "Natsu Dragneel"
country = "Japan"
city = "Tokyo"
age = 25
year = 2000
is_married = False
is_true = True
is_light_on = True
friend_name, master_name, pet_name = "Gray Fullbuster", "Mackarov", "Happy"

#Exercise Level 2
"""
print("*** Used Data Types ***")
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(friend_name))
print(type(master_name))
print(type(pet_name))
"""

"""
print("*** Get the length of first name ***")
len_fname = len(first_name)
print("First Name: ",first_name)
print("Length: ",len_fname)
"""

"""
print("*** Compare the length of first name and last name ***")
len_lname = len(last_name)
print("Last Name: ",last_name)
print("Length: ",len_lname)
if len_fname > len_lname:
    print(len_fname, ">", len_lname)
elif len_fname < len_lname:
    print(len_fname, "<", len_lname)
else:
    print(len_fname, "=", len_lname)
"""

#Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

#Addition
#Add num_one and num_two and assign the value to a variable total
"""
print("*** Addition ***")
nums = [num_one, num_two]
total = sum(nums)
print(str(num_one), "+", str(num_two), "=", str(total))
"""

#Subtraction
#Subtract num_two from num_one and assign the value to a variable diff
"""
print("*** Subtraction ***")
diff = num_two - num_one
print(str(num_two), "-", str(num_one), "=", str(total))
"""

#Multiplication
#Multiply num_two and num_one and assign the value to a variable product
"""
print("*** Multiplication ***")
product = num_two * num_one
print(str(num_two), "*", str(num_one), "=", str(product))
"""

#Division
#Divide num_one by num_two and assign the value to a variable division
"""
print("*** Division ***")
division = num_one / num_two
print(str(num_one), "/", str(num_two), "=", str(division))
"""

#Modulo
#Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
"""
print("*** Modulus ***")
remainder = num_two % num_one
print(str(num_two), "%", str(num_one), "=", str(remainder))
"""

#Exponent
#Calculate num_one to the power of num_two and assign the value to a variable exp
"""
print("*** Exponent ***")
exp = num_one ** num_two
print(str(num_one), "to the power of", str(num_two), "is", str(exp))
"""

#Floor Division
#Find floor division of num_one by num_two and assign the value to a variable floor_division
"""
print("*** Floor Division ***")
floor_division = num_one // num_two
print(str(num_one), "//", str(num_two), "=", str(floor_division))
"""

#Area of the Circle
#Formula: A = pi * r2
# A = area of the circle
# pi = 3.14159
# r2 = radius to the power of 2 (squared)
"""
radius = input("Give me a number: ")
print("Given Radius: ", radius)

num_pi = 3.14159
exp_inpt = int(radius) ** 2 #given number to the power of 2
area_of_circle = num_pi * exp_inpt
print("Area of the Circle: ", area_of_circle)
"""

#Circumference
#Formula: C = 2 * pi * r
# pi = 3.14159
# r2 = radius
"""
circum_of_circle = 2 * num_pi * int(radius)
print("Circumference: ",circum_of_circle)
"""

#User Input
#get first name, last name, country and age from a user
inpt_fname = input("First Name: ")
inpt_lnane = input("Last Name: ")
inpt_country = input("Country: ")
inpt_age = input("Age: ")

str_message = "You're " + inpt_fname + " " + inpt_lnane + ". \n" + inpt_age + "year(s) old, from "+ inpt_country + "!"
print(str_message)