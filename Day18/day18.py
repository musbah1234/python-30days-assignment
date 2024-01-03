from collections import Counter
import re

# Given paragraph
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

# Tokenize the paragraph into words
words = re.findall(r'\b\w+\b', paragraph.lower())

# Count the frequency of each word
word_counts = Counter(words)

# Find the most frequent word
most_frequent_word = word_counts.most_common(1)[0][0]

# Print the result
print("The most frequent word is:", most_frequent_word)


# Given text containing particle positions
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

# Extract numbers from the text
import re
numbers = [int(match) for match in re.findall(r'-?\d+', text)]

# Sort the numbers
sorted_points = sorted(numbers)

# Find the distance between the two furthest particles
distance = sorted_points[-1] - sorted_points[0]

# Print the result
print("Extracted Numbers:", sorted_points)
print("Distance between the two furthest particles:", distance)


import re

def is_valid_variable(variable_name):
    # Define a pattern for a valid Python variable
    pattern = re.compile(r'^[a-zA-Z_][a-zA-Z0-9_]*$')

    # Check if the variable_name matches the pattern
    return bool(pattern.match(variable_name))

# Test cases
print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name'))  # False
print(is_valid_variable('firstname'))  # True


import re
from collections import Counter

def clean_text(text):
    # Remove special characters and digits
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert to lowercase and split into words
    words = cleaned_text.lower().split()
    return ' '.join(words)

def count_most_frequent_words(text, n=3):
    # Clean the text
    cleaned_text = clean_text(text)
    # Tokenize the text into words
    words = cleaned_text.split()
    # Count the occurrences of each word
    word_counts = Counter(words)
    # Get the most common words
    most_common_words = word_counts.most_common(n)
    return most_common_words

# Given sentence
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# Cleaned text
cleaned_text = clean_text(sentence)
print(cleaned_text)

# Count three most frequent words
most_frequent_words = count_most_frequent_words(sentence, n=3)
print(most_frequent_words)

