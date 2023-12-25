# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filtered_numbers = [num for num in numbers if num <= 0]

print("Filtered Numbers:", filtered_numbers)


# Flatten the list of lists of lists to a one-dimensional list using Python

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened_list = [num for sublist in list_of_lists for subsublist in sublist for num in subsublist]

print("Flattened List:", flattened_list)


# Using list comprehension to create the specified list of tuples in Python

result_list = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print("Resulting List of Tuples:")
print(result_list)


# Flatten the list of countries to a new list in the specified format using python

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Use list comprehension to create the flattened list
flattened_countries = [[country[0].upper(), country[0][:3].upper(), country[1].upper()] for sublist in countries for country in sublist]

# Print the resulting list
print("Flattened List of Countries:")
print(flattened_countries)


countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

# Convert list of tuples to list of dictionaries
output = [{'country': country[0][0].upper(), 'city': country[0][1].upper()} for country in countries]

print(output)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

# Convert list of lists to list of concatenated strings
output = [' '.join(name[0]) for name in names]

print(output)

# Lambda function to calculate slope or y-intercept of a linear function
linear_function = lambda x, m, b: m * x + b

# Example usage:
# Calculate the y-value for x=3 with slope (m) of 2 and y-intercept (b) of 1
result = linear_function(3, 2, 1)

# Print the result
print(result)

