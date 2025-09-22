#Day 5: 30 Days of python programming

#Exercise Level 1

#Declare an empty list
my_empty_lst = []

#Declare a list with more than 5 items
the_robinsons = ['john', 'maureen', 'judy', 'penny', 'will', 'robot']

#Find the length of your list
robinsons_head_count = len(the_robinsons)
print(robinsons_head_count)

#Get the first item, the middle item and the last item of the list
first, second, third, fourth, fifth, sixth = the_robinsons
print("First: ", first)
print("Middle: ", third)
print("Last: ", sixth)

#Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['debbie the chicken', '2 years old', '2 ft', 'single', 'jupiter 2']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#Print the list using print()
print("IT Companies: ", it_companies)

#Print the number of companies in the list
num_it_companies = len(it_companies)
print("Number of IT Companies: ",num_it_companies)

#Print the first, middle and last company
first_company_index = 0
last_company_index = num_it_companies - 1
mid_company_index = round(last_company_index / 2)
print("First Company: ", it_companies[first_company_index])
print("Middle Company: ", it_companies[mid_company_index])
print("Last Company: ", it_companies[last_company_index])

#Print the list after modifying one of the companies
it_companies[4] = "Red Hat"
print("New IT Companies: ", it_companies)

#Add an IT company to it_companies
it_companies.append('Canva')

#Insert an IT company in the middle of the companies list
it_companies.insert(mid_company_index, 'Atlassian')
print("New IT Companies 2: ", it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[first_company_index] = it_companies[first_company_index].upper()
print("New IT Companies 3: ", it_companies)

#Join the it_companies with a string '#;  '
extra_str = '#;  '
it_companies_and_string = extra_str.join(it_companies)
print(it_companies_and_string)

#Check if a certain company exists in the it_companies list.
company_to_search = 'Apple'
company_result_index = it_companies.index(company_to_search)

if(company_result_index != 0):
    print(company_to_search, " is found!")
else:
    print(company_to_search, " not found!")

#Sort the list using sort() method
it_companies.sort()
print("Sorted: ", it_companies)

#Reverse the list in descending order using reverse() method
it_companies.reverse()
print("Reversed: ", it_companies)

#Slice out the first 3 companies from the list
first_three_companies = it_companies[0:3]
print("First 3 companies: ", first_three_companies)

#Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]
print('Last 3 companies: ', last_three_companies)