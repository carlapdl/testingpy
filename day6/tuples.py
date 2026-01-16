#Day 6: 30 Days of python programming

#Exercises: Level 1

#Create an empty tuple
my_emtpy_tuple = tuple()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Lucy', 'Erza', 'Evergreen')
brothers = ('Natsu', 'Gray', 'Leon')

#Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
#print(siblings)

#How many siblings do you have?
#print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('Jonathan', 'Nancy')
family_members = siblings + parents
#print(family_members)

#Exercises: Level 2

#Create fruits, vegetables and animal products tuples. 
#Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('saging', 'bayabas', 'lansones', 'mansanas')
veggies = ('sitaw', 'bataw', 'patani', 'labanos', 'mustasa')
animal_products = ('gatas', 'keso', 'itlog', 'mantikilya', 'mantika')
food_stuff_tp = fruits + veggies + animal_products
#print(food_stuff_tp)

#Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
#print(food_stuff_lt)

#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_lst_len = len(food_stuff_lt)
#print(food_lst_len)
food_lst_mid = round(food_lst_len / 2)
#print(food_lst_mid)
food_mid_item = food_stuff_lt[food_lst_mid]
#print(food_mid_item)

#Slice out the first three items and the last three items from food_stuff_lt list
food_first_three = food_stuff_lt[0:3]
#print(food_first_three)
food_last_three = food_stuff_lt[-3:]
#print(food_last_three)

#Delete the food_stuff_tp tuple completely
del food_stuff_tp
#print(food_stuff_tp) #check if still exists

#Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country
#Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
estonia_found = 'Estonia' in nordic_countries
print(f'Estonia is a Nordic country: {estonia_found}')
iceland_found = 'Iceland' in nordic_countries
print(f'Iceland is a Nordic country: {iceland_found}')