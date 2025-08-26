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
"""
str_len1 = len(str1)
str_len2 = len(str2)
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

#Find the length of the text python and convert the value to float and convert it to string