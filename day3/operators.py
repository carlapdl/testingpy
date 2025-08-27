#Day 3: 30 Days of python programming

#Declare your age as integer variable
my_age = 29

#Declare your height as a float variable
my_height = 5.00

#Declare a variable that store a complex number
j = 2
my_complex_num = (1 + 2j)

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
"""
print("*** Area of Triangle ***")
inpt_base = input("Enter Base: ")
my_base = int(inpt_base)
inpt_height = input("Enter Height: ")
my_height = int(inpt_height)
my_tri_area = 0.5 * my_base * my_height
print("Area of Triangle: ", str(my_tri_area))
"""

#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
"""
print("*** Perimeter of Triangle ***")
inpt_a = input("Enter Value for Side A: ")
side_a = int(inpt_a)
inpt_b = input("Enter Value for Side B: ")
side_b = int(inpt_b)
inpt_c = input("Enter Value for Side C: ")
side_c = int(inpt_c)
tri_perimeter = side_a + side_b + side_c
print("Perimeter of Triangle: ", str(tri_perimeter))
"""

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
"""
print("*** A Rectangle ... Bow! ***")
inpt_rec_width = input("Enter value for Width: ")
my_rec_width = int(inpt_rec_width)
inpt_rec_length = input("Enter value for Length: ")
my_rec_length = int(inpt_rec_length)
area_rect = my_rec_length * my_rec_width
perimeter_rect = 2 * (my_rec_length + my_rec_width)
print("Area: ", str(area_rect))
print("Perimeter: ", str(perimeter_rect))
"""

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
"""
print("*** A Circle ... Boing! Boing! ***")
inpt_radius = input("Enter value for Radius: ")
circ_radius = int(inpt_radius)
num_pi = 3.14159
exp_inpt = circ_radius ** 2 #given number to the power of 2
area_of_circle = num_pi * exp_inpt
print("Area: ", area_of_circle)
circum_of_circle = 2 * num_pi * circ_radius
print("Circumference: ",circum_of_circle)
"""

#Calculate the slope, x-intercept and y-intercept of y = 2x -2

#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
"""
my_x1 = 2
my_y1 = 2
my_x2 = 6
my_y2 = 10

d1 = my_x2 - my_x1
d2 = my_y2 - my_y1

my_slope = d2 / d1

exp1 = d1 ** 2 #exponent 2
exp2 = d2 ** 2 #exponent 2

total = exp1 + exp2

my_eucl = total ** 0.5 #get the square root

print("*** Slope and Euclidean ***")
print("Given: point (2, 2) and point (6,10)")
print("Slope: ", my_slope)
print("Euclidean distance: ",my_eucl)
"""

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
str1 = 'python'
str2 = 'dragon'

str_len1 = len(str1)
str_len2 = len(str2)
"""
print(str1, ' chars: ', str(str_len1))
print(str2, ' chars: ', str(str_len2))
print(str(str_len1), 'is not', str(str_len1), str_len1 is not str_len2)
"""

#Use and operator to check if 'on' is found in both 'python' and 'dragon'
"""
print('\'on\' can be found in the words python and dragon')
print('on' in str1 and 'on' in str2)
"""

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
"""
my_sentence = "I hope this course is not full of jargon."
print('This is our sentence: ')
print(my_sentence)
print('Can you see the word \'jargon\'?')
is_jargon_found = 'jargon' in my_sentence
print(is_jargon_found)

#There is no 'on' in both dragon and python
print("There is no \'on\' in both dragon and python.")
print("Is this correct?")

is_on_not_found = 'on' not in str1 and 'on' not in str2
print(is_on_not_found)
"""

#Find the length of the text python and convert the value to float and convert it to string
"""
print('word is: ', str1)
to_str_len = str(str_len1)
print('length as type: ', type(to_str_len), 'value: ', to_str_len)
to_float_len = float(str_len1)
print('length as type: ', type(to_float_len), 'value: ', to_float_len)
"""

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
"""
inpt_num = input("Give me a number, please: ")
given_num = int(inpt_num)
mod_given_num = given_num % 2

if mod_given_num == 0 and inpt_num not in 'python':
    print(inpt_num, ' is even and not in \'python\'.')
else:
    print('bye!')
"""

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
"""
print("*** Check floor division result of 7 and 3 ***")
ans_floor_div = 7 // 3
print('actual floor div: ', ans_floor_div)
to_int_ans = int(ans_floor_div)
print('converted to ', type(to_int_ans), ' = ', to_int_ans)

if to_int_ans == 2.7:
    print('answer is equal to 2.7')
else:
    print('answer is not equal to 2.7')
"""

#Check if type of '10' is equal to type of 10
"""
d_type1 = type('10')
d_type2 = type(10)
print('is ', d_type1, '\'10\'', ' = ', d_type2, str(10), '?: ', d_type1 is d_type2)
"""

#Check if int('9.8') is equal to 10
"""
str_num = '9.8'
check_num = float(str_num)
to_int_check_num = int(check_num)

if(to_int_check_num == 10):
    print(str_num, ' = 10')
else:
    print(str_num, ' not equal to 10')
"""

#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
"""
print("*** How much is your salary? ***")
inpt_hours = input("Enter number of work hours: ")
inpt_rate = input("Enter rate per hour: ")

num_hours = int(inpt_hours)
num_rate = float(inpt_rate)

salary = num_hours * num_rate

print('Your Salary: ', str(salary))
print('There you go, rich kid! :)')
"""

#Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
#1 year = 365.25 days = 31,557,600 seconds
"""
inpt_age= input("Enter your age: ")
num_age = int(inpt_age)

seconds_lived = num_age * 31557600

print("WOW! You're alive for ", str(seconds_lived), 'seconds!')
"""

#Write a Python script that displays the following table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

num_list = []

i = 1
while i <= 5:
    j = 1
    num_list.append(j)
    while len(num_list) < 4:
        j = i * j
        num_list.append(j)
    print("#",str(i), num_list)
    i += 1
    num_list.clear()