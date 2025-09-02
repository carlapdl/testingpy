#Day 4: 30 Days of python programming

#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
"""
the_words = ['Thirty', 'Days', 'Of', 'Python']
the_sentence = ' '.join(the_words)
print(the_sentence)
"""

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
"""
the_words2 = ['Coding', 'For' , 'All']
the_sentence2 = ' '.join(the_words2)
print(the_sentence2)
"""

#Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Coding For All string.
split_str = company.split(" ")
print(split_str[0])

#Check if Coding For All string contains a word Coding using the method index, find or other methods.
sub_str = 'Coding'
if(company.find(sub_str) != -1):
    print(sub_str + ' is found!')
else:
    print(sub_str + ' not found!')

#Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

#Change Python for Everyone to Python for All using the replace method or other methods.
py_sentence = "Python For Everyone"
print("Original Sentence: ", py_sentence)
new_sentece = py_sentence.replace('Everyone', 'All')
print("New Sentence: ", new_sentece)

#Split the string 'Coding For All' using space as the separator (split()) .
print(split_str)

#"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
brands_str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_brands = brands_str.split(",")
print(split_brands)

#What is the character at index 0 in the string Coding For All.
print("String: ", company)
print("First character: ", company[0])

#What is the last index of the string Coding For All.
company_lst_index = len(company) - 1
print("Last index: ", company_lst_index)

#What character is at index 10 in "Coding For All" string.
print(company[10])

# create_abrv
# - function to create an accronym / abbreviation of the given phrase (my_phrase)
def create_abrv(my_phrase):
    splt_sentence = my_phrase.split(" ")
    words_cnt = len(splt_sentence)

    i = 0
    my_abrv = ""
    while(i < words_cnt):
        my_word = splt_sentence[i]
        my_abrv = my_abrv + my_word[0] + '.'
        i += 1

    print(my_phrase + " (" + my_abrv + ")")

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
create_abrv(py_sentence)

#Create an acronym or an abbreviation for the name 'Coding For All'.
create_abrv(company)

# find_me
# - find the first or last occurence of the given string
# args:
#   - needle : given string / what to look for
#   - haystack : string / where to look at
#   - order: value = 'first' or 'last'
def find_me(needle, haystack, order):
    print(f"Haystack: {haystack}")
    if(order == 'first'):
        print("checking for first occurence ...")
        my_index = haystack.index(needle)
    elif(order == 'last'):
        print("checking for last occurence ...")
        my_index = haystack.rindex(needle)
    else:
        print("incomplete instruction")
        exit

    if(my_index != -1):
        print(f"{needle} found at index: {str(my_index)}")
    else:
        print(f"{needle} not found in {haystack}")

#Use index to determine the position of the first occurrence of C in Coding For All.
find_me('C', company, 'first')

#Use index to determine the position of the first occurrence of F in Coding For All.
find_me('F', company, 'first')

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
str_cfap = "Coding For All People"
find_me("l", str_cfap, 'last')

#Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
long_phrase = "You cannot end a sentence with because because because is a conjunction."
find_me('because', long_phrase, 'first')

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
find_me('because', long_phrase, 'last')

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
to_remove = "because"
cleaned_phrase = long_phrase.replace(to_remove, "")
print(f"Removing \'{to_remove}\' ... ")
print(f"Cleaned phrase: {cleaned_phrase}")

#Does ''Coding For All' start with a substring Coding?
#Does 'Coding For All' end with a substring coding?
sub_str = 'Coding'
sub_index = company.find(sub_str)
if(sub_index == 0):
    print(f'{company} starts with \'{sub_str}\'')
elif(sub_index == company_lst_index):
    print(f'{company} ends with \'{sub_str}\'')
else:
    print(f'{company} doesn\'t start or end with \'{sub_str}\'')

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
str_to_clean = '   Coding For All      '
print(f'Cleaning \'{str_to_clean}\' ...')
clean_str = str_to_clean.lstrip()
clean_str = clean_str.rstrip()
print(f'Clean string: \'{clean_str}\'')

#Which one of the following variables return True when we use the method isidentifier()?
given_str1 = '30DaysOfPython'
given_str2 = 'thirty_days_of_python'

if(given_str1.isidentifier()):
    print(f'{given_str1} IS an identifier')
else:
    print(f'{given_str1} IS NOT an identifier')

if(given_str2.isidentifier()):
    print(f'{given_str2} IS an identifier')
else:
    print(f'{given_str2} IS NOT an identifier')

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
#Join the list with a hash with space string.
py_libs = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
lst_py_libs = '# '.join(py_libs)
print(lst_py_libs)

#Use the new line escape sequence to separate the following sentences.
line1 = 'I am enjoying this challenge.' 
line2 = 'I just wonder what is next.'

print(f'\n{line1}')
print(f'{line2}\n')

#Use a tab escape sequence to write the following lines.
tabline1= 'Name\tAge\tCountry\tCity\n'
tabline2 = 'Asabeneh\t250\tFinland\tHelsinki\n'

print(f'{tabline1.expandtabs(10)}')
print(f'{tabline2.expandtabs(1)}')

#Use the string formatting method to display the following:
radius = 10
pi = 3.14
area = pi * radius ** 2

print(f'\n radius = {radius}')
print(f'\n pi = {pi}')
print(f'\n area = {pi} * {radius} ** 2')
print(f'\n The area of a circle with radius {radius} is {area} square meters.')