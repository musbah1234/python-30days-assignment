# Day 2: 30 Days of python programming

first_name = ("Musbah")
last_name = ("Yakubu")
full_name = ("Musbahu umar yakubu")
country = ("Nigeria")
city = ("kano")
age = (30)
year = (2023)
is_married = True
is_light_on = False

# Declaration of variables in one line.

first_name, last_name, country, age, is_married = 'Musbah', 'Yakubu', 'Nigeria', 30, True

# finding the length of your first name

print(len(first_name))

#compare the length of the first_name and the last_name

first_name_length = len(first_name)
last_name_length = len(last_name)

if first_name_length == last_name_length:
 print("the lenght of the first name and the last name are equal")
else:
 print("The length of the first name and the last name are not equal")

 # Declaring 5 as num_one and 4 as num_two

num_one = 5
num_two = 4

Add = num_one + num_two
Total = Add
print(Total)

Subtract = num_one - num_two
diff = Subtract
print(diff)

Multiply = num_one * num_two
product = Multiply
print(product)

Divide = num_one / num_two
division = Divide
print(division)

mudulo = num_one % num_two
reminder = mudulo
print(reminder)

power = num_one ** num_two
exp = power
print(exp)

floorDivision = num_one // num_two
floor_division = floorDivision
print(floor_division)

# Calculate the area of a circle 
# The radius of a circle is 30 meters
# THe formula is Area = pi r * r**2

Area = 3.1 * (30**2)
area_of_circle = Area
print(area_of_circle)

# circumference of a circle
# the formula is c = 2pi r

circumference = 2 * 3.1 * ( 30)
circum_of_circle = circumference
print (circum_of_circle)

# calculate the area.
# The formular is A = pi r**2

radius = float(input("Enter the radius of the circle: "))
area = 3.1 * (radius**2)
print(f"The area of the circle with radius {radius} is: {area}")

# Using the built-in input function to get first name ....

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = input("Enter your age: ")

print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Country: {country}")
print(f"Age: {age}")

