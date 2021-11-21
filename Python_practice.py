print("Hello World")

# type() to determine the data type
print(type(3))

#Variable Types
num_candidates = 3 #integer
winning_percentage = 73.81 #Flaot
candidate = "Diane" #String
won_election = True #Bool

#help("Keywords") for reserved words
# Operators: + - * / % // **

#Creating a list, indexing starts at 0 (1 less than the number of the items in list)
my_list = []
my_list2 = list()
counties = ["Arapahoe","Denver","Jefferson"]

#Negative indexes are used to identify a list items position relative to the end of the list
# Last item is -1
# Second to last is -2

#Length of the list
len(counties)

#Slicing is used to get specific items from the list
#list[start:end], Start refers to the index of the first item in slice, end refers to the last item,
#Expression returns copy conting items between the 2 index from list (NOT INCLUDING THE END)

counties[0:2] #Arapoe Denver or type counties[:2]
counties[1:] #Denver and jefferson


#Adding items to the list
#list.append()
counties.append("El Paso")

#To specify, list.insert(index,obj)
counties.insert(2,"El Paso")

#To remove, we use.remove
counties.remove("El Palso")
counties.pop(3)

#Can use .pop 2, tells u what value been removed

#Tuples are similar to list but cannot be changed, cannot add or remove items from them

my_tuple=()
my_tuple2= tuple()
counties_tuple = ("Arapahoe","Denver","Jefferson")

#Creating a dictionaries
#Its an object that sores a collection of data {Key:Value} or {key1:value1, key2:value2}
my_dictionary ={}
my_dic = dict()

#Dictionary
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

#Retreive items
counties_dict.items() #Cannot use list indexing 
counties_dict.keys() #list keys
counties_dict.values() #list values
counties_dict.get("Denver") #Gets a specific value

#All valid ways, they do the same thing (gets the number of voters for county araphahoe)
counties_dict['Arapahoe'] 

counties_dict.get("Arapahoe")  

print(counties_dict['Arapahoe'])  

print(counties_dict.get("Arapahoe")) 

#Creating a list of dictionaries  (when keys assosciiated with different values)
# [{key1:value1, key2:value2}, {key1:value3, key2:value4}]
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

#[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}

#if condition:
  # statement 1
   #statement 2

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])



temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


#In Statement

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


#Loops
# while (CONDITION):
x = 0
while x <= 5:
    print(x)
    x = x + 1

#for item in [items]:
    #statement 1
    #statement 2


for county in counties:
    print(county)

for i in range(len(counties)): #Range the # of counties
    print(counties[i])


numbers =[0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)


#Iteration for dictionary:
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict: #Getting only the keys
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values(): #Getting the values
    print(voters)

for county in counties_dict:
    print(counties_dict[county]) #""

for county in counties_dict:
    print(counties_dict.get(county)) #""

#for key, value in dictionary_name.items(): #Get keys and values
    #print(key, value)

for county, voters in counties_dict.items():
    print(county, voters)


#Printing list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#{'county': 'Arapahoe', 'registered_voters': 422829}
#{'county': 'Denver', 'registered_voters': 463353}
#{'county': 'Jefferson', 'registered_voters': 432438}

#To Retreive the values from a list of dictionaries we must use a nested for loop
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#Arapahoe
#422829
#Denver
#463353
#Jefferson
#432438

#For only county name use this:
for county_dict in voting_data:
    print(county_dict['county'])

#To print numbers
#rint("TEXT" + str(VARIABLE))

#F strings, automatic concatenation and can perform calcyulations
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#VS

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#With dictionaries

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#VS

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multiline fstrings
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)


#Formatting 
#'{value:{width}.{precision}}'



# Importing dependencies
import csv
import os #Allows us to interact with Operating System

#print(dir(os))


# Importing Election Results
file_to_load = 'Resources/election_results.csv'
os.path.join("Resources", "election_results.csv")
file_to_load = os.path.join("Resources", "election_results.csv")

# Open the Election Results and read the file
#election_data = open(file_to_load,'r') Method 1
with open(file_to_load) as election_data:

    # To do: Perform Analysis
    print(election_data)





# Close the File Method 1
#election_data.close()

# Using the open() function with the "w" mode we will write data to the file.
With open(file_to_save, "w")

# Write Some Data to the File. 
outfile.write("Hello World")

# Close the file
outfile.close()