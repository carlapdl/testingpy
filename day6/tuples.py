#Day 6: 30 Days of python programming

#Exercises: Level 1

#Create an empty tuple
my_emtpy_tuple = tuple()

#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Lucy', 'Erza', 'Evergreen')
brothers = ('Natsu', 'Gray', 'Leon')

#Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

#How many siblings do you have?
print(len(siblings))

#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings = list(siblings)
siblings[0] = 'Makarov'
siblings[1] = 'Nonoka'
siblings = tuple(siblings)
print(siblings)