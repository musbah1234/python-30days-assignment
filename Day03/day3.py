'''
age = 30
height = 1.7
complex_num = 2 + 2j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = float(input("Enter base:"))
Height = float(input("Enter height:"))
area = 0.5 * ( base * Height )
area_as_integer = int(area)
print (f"The area of a triangle is: {area_as_integer}")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
# Calculate the perimeter of the triangle (perimeter = a + b + c).

a = int(input("Enter side a:"))
b = int(input("Enter side b:"))
c = int(input("Enter side c:"))
perimeter = a + b + c
print(f"The perimeter of a triangle is: {perimeter}")

# Get length and width of a rectangle using prompt.
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = int(input("Enter the length:"))
width = int(input("Enter the width:"))
rec_area = length * width
rec_perimeter = 2 * (length + width)
print (f"The area of a rectangle is: {rec_area} \nAnd the perimeter of a rectangle is: {rec_perimeter}")
 
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius =  int(input("Enter radius"))
cir_area = 3.14 * ( radius**2 )
cir_circumference = 2 * 3.14 * (radius)
print (f"The area of a circle is: {cir_area} \nAnd the circumference of a circle is: {cir_circumference}")


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Equation: y = 2x - 2

slope = 2

x_intercept = 2 / slope

y_intercept = -2

print(f"Slope (m): {slope}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

import math

# Coordinates of the points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Slope (m)
slope = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Slope (m): {slope}")
print(f"Euclidean Distance: {distance}")

# Compare the slopes in tasks 8 and 9.

import math

# Coordinates of the points for Task 8
x1_task8, y1_task8 = 2, 2
x2_task8, y2_task8 = 6, 10

# Slope calculation for Task 8
slope_task8 = (y2_task8 - y1_task8) / (x2_task8 - x1_task8)

# Coordinates of the points for Task 9
x1_task9, y1_task9 = 1, 3
x2_task9, y2_task9 = 5, 7

# Slope calculation for Task 9
slope_task9 = (y2_task9 - y1_task9) / (x2_task9 - x1_task9)

# Comparing slopes
if slope_task8 > slope_task9:
    comparison_result = "The slope in Task 8 is greater than the slope in Task 9."
elif slope_task8 < slope_task9:
    comparison_result = "The slope in Task 8 is less than the slope in Task 9."
else:
    comparison_result = "The slopes in Task 8 and Task 9 are equal."

# Printing the results
print(f"Slope in Task 8: {slope_task8}")
print(f"Slope in Task 9: {slope_task9}")
print(comparison_result)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

import cmath  # Import the complex math module for handling complex roots

def find_roots(a, b, c):
    # Calculate the discriminant
    d = cmath.sqrt(b**2 - 4*a*c)

    # Find the roots using the quadratic formula
    root1 = (-b + d) / (2*a)
    root2 = (-b - d) / (2*a)

    return root1, root2

# Coefficients of the quadratic equation
a = 1
b = 6
c = 9

# Find the roots
roots = find_roots(a, b, c)

# Print the roots
print(f"The roots of the quadratic equation are: {roots}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.

# Strings
python_str = 'python'
dragon_str = 'dragon'

# Find the length of strings
python_length = len(python_str)
dragon_length = len(dragon_str)

# Falsy comparison statement
falsy_comparison = python_length == dragon_length

# Print the results
print(f"The length of 'python' is {python_length}")
print(f"The length of 'dragon' is {dragon_length}")
print(f"Falsy comparison statement: {falsy_comparison}")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'

python_str = 'python'
dragon_str = 'dragon'

# Check if 'on' is present in both strings using the `and` operator
is_on_in_both = 'on' in python_str and 'on' in dragon_str

# Print the result
print(f"Is 'on' present in both 'python' and 'dragon'? {is_on_in_both}")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

sentence = "I hope this course is not full of jargon"

is_jargon_present = "jargon" in sentence

print(f"Is jargon present in the sentence? {is_jargon_present}")

# There is no 'on' in both dragon and python

python_str = 'python'
dragon_str = 'dragon'
is_no_on_in_both = 'on' not in python_str and "on" not in dragon_str

print(f"There is no 'on' in both dragon and python? {is_no_on_in_both}")

# Find the length of the text python and convert the value to float and convert it to string

text = "python"
length_of_text = len(text)

length_as_float = float(length_of_text)
length_as_string = str(length_of_text)

print(f"length of python: {text}")
print(f"length as float: {length_as_float}")
print(f"length of string: {length_as_string}")


# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

num = int(input("Enter a number:"))
if num % 2 == 0:
 print("The number is even ")
else: 
 print("The number is odd")
 
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# Perform floor division of 7 by 3
floor_division_result = 7 // 3

# Convert 2.7 to an integer
int_value = int(2.7)

# Check if the floor division result is equal to the integer value
if floor_division_result == int_value:
    print(f"The floor division of 7 by 3 is equal to the int converted value of 2.7.")
else:
    print(f"The floor division of 7 by 3 is not equal to the int converted value of 2.7.")

# Check if type of '10' is equal to type of 10

num1 = '10'
num2 = 10

num1_type = type(num1)
num2_type = type(num2)
if num1_type == num2_type:
    print("both are equal")
else:
    print("both are different")    

# Check if int('9.8') is equal to 10

# Convert the floating-point number 9.8 to an integer
converted_value = int(9.8)

# Check if the converted value is equal to 10
if converted_value == 10:
    print("The integer value of 9.8 is equal to 10.")
else:
    print("The integer value of 9.8 is not equal to 10.")

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hour = int(input("Enter hour:"))
rate_per_hour = int(input("Enter rate per hour:"))

pay = hour * rate_per_hour
print(f"Your weekly earning is: {pay}")

# Write a script that prompts the user to enter number of years.
#  Calculate the number of seconds a person can live. Assume a person can live hundred years

num_of_years = int(input("Enter years:"))
seconds = num_of_years * 60 * 60 * 24 * 365

print(f"you lived for {seconds} seconds")
'''
# Write a Python script that displays

print("1 1 1 1 1  \n2 1 2 4 8 \n3 1 3 9 27 \n4 1 4 16 64 \n5 1 5 25 125" )






