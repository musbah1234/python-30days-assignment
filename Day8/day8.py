# Create an empty dictionary called 'dog'
dog = {}

# Add attributes to the 'dog' dictionary
dog["name"] = "Buddy"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 3

# Create a 'student' dictionary
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 20,
    "marital_status": "Single",
    "skills": ["Programming", "Data Analysis"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main St"
}

# Get the length of the 'student' dictionary
student_length = len(student)

# Get the value of 'skills' and check the data type
skills_value = student["skills"]
skills_data_type = type(skills_value)

# Modify 'skills' values by adding one or two skills
student["skills"].extend(["Communication", "Problem Solving"])

# Get the dictionary keys and values as lists
keys_list = list(student.keys())
values_list = list(student.values())

# Change the dictionary to a list of tuples using items() method
student_tuples = list(student.items())

# Delete one of the items in the dictionary
del student["marital_status"]

# Delete the 'dog' dictionary
del dog

# Print the results
print(f"Length of 'student' dictionary: {student_length}")
print(f"Data type of 'skills' in 'student' dictionary: {skills_data_type}")
print(f"Modified 'skills' values: {student['skills']}")
print(f"Dictionary keys: {keys_list}")
print(f"Dictionary values: {values_list}")
print(f"Dictionary as a list of tuples: {student_tuples}")
