# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years. 

age = int(input("Enter your Age:"))

if age >= 18:
    print("You are old enough to drive")
else:
    Below = 18 - age
    print(f"You need {Below} more years to learn to drive")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age. Output:
    
me = int(input("Enter your age:"))
you = int(input("Enter your age:"))

if me > you:
    age_diff = me - you
    if age_diff == 1:
        print("you are 1 year older than me")
    else:
        print(f"you are {age_diff} years older than me")
elif you > me:
    age_diff = you - me
    if age_diff == 1:
        print("I am 1 year older than you")
    else:
        print(f"i am {age_diff} years older than you")


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b,
# if a is less b return a is smaller than b, else a is equal to b

# Get two numbers from the user using input prompt
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Compare the numbers
if a > b:
    print(f"{a} is greater than {b}")
elif a < b:
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")


# Write a code which gives grade to students according to theirs scores:
'''
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
'''

# Get the student's score as input
score = float(input("Enter the student's score: "))

# Assign grades based on the score range
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 89:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = 'Invalid score, please enter a score between 0 and 100.'

# Print the assigned grade
print(f"The student's grade is: {grade}")



#Check if the season is Autumn, Winter, Spring or Summer. 
#If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. 
# March, April or May, the season is Spring June, July or August, the season is Summer


# Get user input for month
user_month = input("Enter the month: ").capitalize()

# Check the season based on the user input
if user_month in ["September", "October", "November"]:
    season = "Autumn"
elif user_month in ["December", "January", "February"]:
    season = "Winter"
elif user_month in ["March", "April", "May"]:
    season = "Spring"
elif user_month in ["June", "July", "August"]:
    season = "Summer"
else:
    season = "Invalid month, please enter a valid month."

# Print the determined season
print(f"The season for {user_month} is: {season}")


# The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# If the fruit exists print('That fruit already exist in the list')

# List of fruits
fruits = ['banana', 'orange', 'mango', 'lemon']

# Get user input for a new fruit
new_fruit = input("Enter a new fruit: ")

# Convert input to lowercase for case-insensitivity
new_fruit = new_fruit.lower()

# Check if the new fruit exists in the list
if new_fruit not in fruits:
    # If it doesn't exist, add it to the list
    fruits.append(new_fruit)
    print("Modified list:", fruits)
else:
    # If it exists, print a message
    print("That fruit already exists in the list.")

# Note: This code assumes a case-insensitive check for existing fruits.



# Modified Person Dictionary
person = {
    'first_name': 'Musbah',
    'last_name': 'Umar',
    'age': 30,
    'country': 'Nigeria',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Amarawa street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has 'skills' key
if 'skills' in person:
    # Print out the middle skill in the skills list
    skills_list = person['skills']
    if len(skills_list) % 2 != 0:
        middle_skill = skills_list[len(skills_list) // 2]
        print(f"Middle skill in the skills list: {middle_skill}")

    # Check if the person has 'Python' skill and print the result
    if 'Python' in skills_list:
        print("Person has 'Python' skill.")

    # Check for developer title based on skills
    if skills_list == ['JavaScript', 'React']:
        print("He is a front-end developer.")
    elif set(['Node', 'Python', 'MongoDB']).issubset(skills_list):
        print("He is a backend developer.")
    elif set(['React', 'Node', 'MongoDB']).issubset(skills_list):
        print("He is a full-stack developer.")
    else:
        print("Unknown title.")

# Check if the person is married and lives in Nigeria
if person.get('is_married') and person.get('country') == 'Nigeria':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
