# Writ a function which generates a six digit/character random_user_id.
import random
import string

def generate_random_user_id():
    # Generate a random string of six characters from uppercase letters and digits
    random_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return random_id

print(generate_random_user_id())


# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

import random
import string

def user_id_gen_by_user():
    # Take user input for the number of characters
    num_characters = int(input("Enter the number of characters for each user ID: "))
    
    # Take user input for the number of IDs to be generated
    num_ids = int(input("Enter the number of IDs to generate: "))
    
    # Generate user IDs based on user inputs
    user_ids = []
    for _ in range(num_ids):
        user_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num_characters))
        user_ids.append(user_id)
    
    return user_ids

# Example usage
generated_user_ids = user_id_gen_by_user()
print("Generated User IDs:", generated_user_ids)

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).

import random

def rgb_color_gen():
    # Generate random values for Red, Green, and Blue in the range 0 to 255
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    
    # Return the generated RGB color as a tuple
    return red, green, blue

# Example usage
generated_color = rgb_color_gen()
print("Generated RGB Color:", generated_color)



import random

def list_of_hexa_colors(num_colors):
   
    hex_colors = ['#' + ''.join([random.choice('0123456789ABCDEF') for _ in range(6)]) for _ in range(num_colors)]
    return hex_colors

def list_of_rgb_colors(num_colors):
  
    rgb_colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(num_colors)]
    return rgb_colors

def generate_colors(num_colors, color_type='hexa'):
   
    if color_type == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("Invalid color type. Use 'hexa' or 'rgb'.")


hex_colors = generate_colors(5, color_type='hexa')
rgb_colors = generate_colors(5, color_type='rgb')

print("Generated Hexadecimal Colors:", hex_colors)
print("Generated RGB Colors:", rgb_colors)


# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

import random

def shuffle_list(input_list):
    
    shuffled_list = input_list.copy()
    random.shuffle(shuffled_list)
    return shuffled_list

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def generate_unique_random_numbers():
    
    unique_numbers = random.sample(range(10), 7)
    return unique_numbers


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffled_result = shuffle_list(original_list)
unique_random_numbers = generate_unique_random_numbers()

print("Original List:", original_list)
print("Shuffled List:", shuffled_result)
print("Unique Random Numbers:", unique_random_numbers)


