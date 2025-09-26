#Day 5: 30 Days of python programming

#Exercise Level 1

#Declare an empty list
my_empty_lst = []

#Declare a list with more than 5 items
the_robinsons = ['john', 'maureen', 'judy', 'penny', 'will', 'robot']

#Find the length of your list
robinsons_head_count = len(the_robinsons)
#print(robinsons_head_count)

#Get the first item, the middle item and the last item of the list
first, second, third, fourth, fifth, sixth = the_robinsons
#print("First: ", first)
#print("Middle: ", third)
#print("Last: ", sixth)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['debbie the chicken', '2 years old', '2 ft', 'single', 'jupiter 2']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()
#print("IT Companies: ", it_companies)

#Print the number of companies in the list
num_it_companies = len(it_companies)
#print("Number of IT Companies: ",num_it_companies)

#Print the first, middle and last company
first_company_index = 0
last_company_index = num_it_companies - 1
mid_company_index = round(last_company_index / 2)
#print("First Company: ", it_companies[first_company_index])
#print("Middle Company: ", it_companies[mid_company_index])
#print("Last Company: ", it_companies[last_company_index])

#Print the list after modifying one of the companies
it_companies[4] = "Red Hat"
#print("New IT Companies: ", it_companies)

#Add an IT company to it_companies
it_companies.append('Canva')

#Insert an IT company in the middle of the companies list
it_companies.insert(mid_company_index, 'Atlassian')
#print("New IT Companies 2: ", it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[first_company_index] = it_companies[first_company_index].upper()
#print("New IT Companies 3: ", it_companies)

#Join the it_companies with a string '#;  '
extra_str = '#;  '
it_companies_and_string = extra_str.join(it_companies)
#print(it_companies_and_string)

#Check if a certain company exists in the it_companies list.
company_to_search = 'Apple'
company_result_index = it_companies.index(company_to_search)
"""
if(company_result_index != 0):
    print(company_to_search, " is found!")
else:
    print(company_to_search, " not found!")
"""

#Sort the list using sort() method
it_companies.sort()
#print("Sorted: ", it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
#print("Reversed: ", it_companies)

#Slice out the first 3 companies from the list
first_three_companies = it_companies[0:3]
#print("First 3 companies: ", first_three_companies)

#Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
#print('Last 3 companies: ', last_three_companies)

#Slice out the middle IT company or companies from the list
new_company_mid_index = round(len(it_companies) / 2)
slice_mid_company = it_companies[new_company_mid_index]
#print("The mid company: ", slice_mid_company)

#Remove the first IT company from the list
del it_companies[0]
#print("Removed first company: ", it_companies)

#Remove the middle IT company or companies from the list
new_company_mid_index_b = round(len(it_companies) / 2)
del it_companies[new_company_mid_index_b]
#print("Removed mid company: ", it_companies)

#Remove the last IT company from the list
del it_companies[-1]
#print("Removed last company: ", it_companies)

#Remove all IT companies from the list
it_companies.clear()
#print(it_companies)

#Destroy the IT companies list
del it_companies
#print(it_companies)

#Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
frontend_backend = front_end + back_end
#print(frontend_backend)

#After joining the lists (front_end, back_end), copy the joined list and assign it to a variable full_stack, 
#then insert Python and SQL after Redux.
full_stack = frontend_backend.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index+1, 'Python')
python_index = full_stack.index('Python')
full_stack.insert(python_index+1, 'SQL')
#print("Full Stack: ", full_stack)

#Exercise Level 2

#The following is a list of 10 students ages:
#* Sort the list and find the min and max age
#* Add the min age and the max age again to the list
#* Find the median age (one middle item or two middle items divided by two)
#* Find the average age (sum of all items divided by their number )
#* Find the range of the ages (max minus min)
#* Compare the value of (min - average) and (max - average), use abs() method

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
sorted_ages = sorted(ages)
print(f"Sorted Age List: {sorted_ages}")

min_age = min(sorted_ages)
max_age = max(sorted_ages)
print(f"Minimum Age: {min_age}")
print(f"Maximum Age: {max_age}")

total_items = len(sorted_ages)
print(f"Total items: {total_items}")

mid_age_item_index = round((total_items - 1) / 2)
#print("Mid Age Index: ", mid_age_item_index)
mid_age_item = sorted_ages[mid_age_item_index]
print(f"Median Age: {mid_age_item}")

total_age = 0
for age_item in sorted_ages:
    total_age = total_age + age_item

#print("Total Age: ", total_age)
ave_age = round(total_age / total_items)
print(f"Average Age: {ave_age}")
print(f"Age Ranges: {max_age - min_age}")
print(f"Abs Min. Average: {abs(min_age - ave_age)}")
print(f"Abs Max. Average: {abs(max_age - ave_age)}")

countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

print(f"Countries: {countries_list}")
#Find the middle country(ies)
total_country_items = len(countries_list)
last_country_index = total_country_items - 1
mid_country_index = round(last_country_index / 2)
print(f"Mid Country: {countries_list[mid_country_index]}")

#Divide the countries list into two equal lists if it is even if not one more country for the first half.
print(f"First Half Country: {countries_list[0:(mid_country_index+1)]}")
print(f"Next Half Countries: {countries_list[(mid_country_index+1):total_country_items]}")

#Unpack the first three countries and the rest as scandic countries.
print(f"First 3 Countries: {countries_list[0:3]}")
print(f"Scandic Countries: {countries_list[(-mid_country_index):]}")