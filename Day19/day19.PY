# Change the function definition to accept a file path as a parameter
def count_lines_and_words(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0

    # Open the file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Count lines
            line_count += 1

            # Count words
            words = line.split()
            word_count += len(words)

    # Return the results
    return line_count, word_count

# Specify the file path for the Obama speech
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/obama_speech.txt'

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")


#b
def count_lines_and_words(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0

    # Open the file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Count lines
            line_count += 1

            # Count words
            words = line.split()
            word_count += len(words)

    # Return the results
    return line_count, word_count

# Specify the file path for the Michelle Obama speech
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/michelle_obama_speech.txt'  # Replace with the actual path to your file

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")

#c

def count_lines_and_words(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0

    # Open the file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Count lines
            line_count += 1

            # Count words
            words = line.split()
            word_count += len(words)

    # Return the results
    return line_count, word_count

# Specify the file path for the Donald Trump speech
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/donald_speech.txt'  # Replace with the actual path to your file

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")



def count_lines_and_words(file_path):
    # Initialize counters
    line_count = 0
    word_count = 0

    # Open the file and iterate through each line
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Count lines
            line_count += 1

            # Count words
            words = line.split()
            word_count += len(words)

    # Return the results
    return line_count, word_count

# Specify the file path for the Melania Trump speech
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/melina_trump_speech.txt'  # Replace with the actual path to your file

# Call the function and get the results
lines, words = count_lines_and_words(file_path)

# Print the results
print(f"Number of lines: {lines}")
print(f"Number of words: {words}")




import json

def get_most_spoken_languages(file_path):
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    # Extract languages and their speakers from the data
    languages_speakers = {}
    for country in countries_data:
        # Check if 'languages' is a dictionary before using items()
        if isinstance(country.get('languages', {}), dict):
            for language, speakers in country['languages'].items():
                if language in languages_speakers:
                    languages_speakers[language] += speakers
                else:
                    languages_speakers[language] = speakers

    # Sort languages by the number of speakers in descending order
    sorted_languages = sorted(languages_speakers.items(), key=lambda x: x[1], reverse=True)

    # Get the top ten languages
    top_ten_languages = sorted_languages[:10]

    return top_ten_languages

# Specify the file path for the countries_data.json file
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/countries_data.json'  # Replace with the actual path to your file

# Call the function and get the results
most_spoken_languages = get_most_spoken_languages(file_path)

# Print the results
print("Ten Most Spoken Languages:")
for language, speakers in most_spoken_languages:
    print(f"{language}: {speakers} speakers")


import json

def get_ten_most_populated_countries(file_path):
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        countries_data = json.load(file)

    # Extract country and population information
    country_population = [(country['name'], country['population']) for country in countries_data]

    # Sort countries based on population in descending order
    sorted_countries = sorted(country_population, key=lambda x: x[1], reverse=True)

    # Get the top ten most populated countries
    top_ten_countries = sorted_countries[:10]

    return top_ten_countries

# Specify the file path for the countries_data.json file
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/countries_data.json'  # Replace with the actual path to your file

# Call the function and get the results
ten_most_populated_countries = get_ten_most_populated_countries(file_path)

# Print the results
print("Ten Most Populated Countries:")
for country, population in ten_most_populated_countries:
    print(f"{country}: {population} population")




import re

def extract_email_addresses(file_path):
    # Open and read the text file
    with open(file_path, 'r', encoding='utf-8') as file:
        text_content = file.read()

    # Define a regular expression pattern for extracting email addresses
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    # Use re.findall to extract all email addresses from the text
    email_addresses = re.findall(email_pattern, text_content)

    return email_addresses

# Specify the file path for the email_exchange_big.txt file
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/email_exchanges.txt'  # Replace with the actual path to your file

# Call the function and get the list of email addresses
email_list = extract_email_addresses(file_path)

# Print the extracted email addresses
print("Extracted Email Addresses:")
for email in email_list:
    print(email)






from collections import Counter
import re

def find_most_common_words(text, num_words):
    # Check if the input is a file path; if so, read the file
    if re.match(r'^\S+\.txt$', text):
        with open(text, 'r', encoding='utf-8') as file:
            text = file.read()

    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the most common words
    most_common_words = word_counts.most_common(num_words)

    return most_common_words

# Example usage with a string
sample_text = "This is a sample text. It contains some words, and some words may repeat."
result = find_most_common_words(sample_text, 5)
print(result)

# Example usage with a file
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/email_exchanges.txt'  # Replace with the actual path to your file
result_from_file = find_most_common_words(file_path, 10)
print(result_from_file)






from collections import Counter
import re

def find_most_frequent_words(text, num_words):
    # Check if the input is a file path; if so, read the file
    if re.match(r'^\S+\.txt$', text):
        with open(text, 'r', encoding='utf-8') as file:
            text = file.read()

    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the most common words
    most_common_words = word_counts.most_common(num_words)

    return most_common_words

# Example usage for Obama's speech
obama_speech_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/obama_speech.txt'  # Replace with the actual path to Obama's speech file
obama_result = find_most_frequent_words(obama_speech_path, 10)
print("Ten most frequent words in Obama's speech:", obama_result)

# Example usage for Michelle's speech
michelle_speech_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/michelle_obama_speech.txt'  # Replace with the actual path to Michelle's speech file
michelle_result = find_most_frequent_words(michelle_speech_path, 10)
print("Ten most frequent words in Michelle's speech:", michelle_result)

# Example usage for Trump's speech
trump_speech_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/donald_speech.txt'  # Replace with the actual path to Trump's speech file
trump_result = find_most_frequent_words(trump_speech_path, 10)
print("Ten most frequent words in Trump's speech:", trump_result)

# Example usage for Melania's speech
melania_speech_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/melina_trump_speech.txt'  # Replace with the actual path to Melania's speech file
melania_result = find_most_frequent_words(melania_speech_path, 10)
print("Ten most frequent words in Melania's speech:", melania_result)

import sklearn
print(sklearn.__version__)



import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

def clean_text(text):
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    return cleaned_text

def remove_support_words(text, stop_words):
    # Remove stop words from the text
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

def check_text_similarity(text1, text2):
    # Vectorize the texts using TF-IDF
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])

    # Calculate cosine similarity
    similarity = cosine_similarity(vectors)

    return similarity[0][1]

def main():
    # Load stop words from the data directory
    stop_words_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/stop_words.py'
    with open(stop_words_path, 'r') as file:
        stop_words = set(file.read().split())

    # Load Michelle's speech
    michelle_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/michelle_obama_speech.txt'
    with open(michelle_path, 'r', encoding='utf-8') as file:
        michelle_speech = file.read()

    # Load Melania's speech
    melania_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/melina_trump_speech.txt'
    with open(melania_path, 'r', encoding='utf-8') as file:
        melania_speech = file.read()

    # Clean and remove stop words
    cleaned_michelle = remove_support_words(clean_text(michelle_speech), stop_words)
    cleaned_melania = remove_support_words(clean_text(melania_speech), stop_words)

    # Check similarity
    similarity_score = check_text_similarity(cleaned_michelle, cleaned_melania)
    print(f"Similarity between Michelle's and Melania's speech: {similarity_score:.2f}")

if __name__ == "__main__":
    main()




from collections import Counter
import re

# Read the text from the file
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/romeo_and_juliet.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Clean the text by removing non-alphanumeric characters and converting to lowercase
cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()

# Tokenize the text into words
words = cleaned_text.split()

# Use Counter to count the occurrences of each word
word_counts = Counter(words)

# Get the 10 most common words
top_10_words = word_counts.most_common(10)

# Print the results
for word, count in top_10_words:
    print(f'{word}: {count} times')





    import pandas as pd

# Read the Hacker News CSV file (replace 'hacker_news.csv' with the actual file path)
file_path = '/home/musbah/projects/Data-Science-Assingment/python-30days-assignment/data/hacker_news.csv'
df = pd.read_csv(file_path)

# Count the number of lines containing 'python' or 'Python'
python_lines = df[df['title'].str.contains('python|Python', na=False, case=False)]
count_python_lines = len(python_lines)

# Count the number of lines containing 'JavaScript', 'javascript', or 'Javascript'
javascript_lines = df[df['title'].str.contains('JavaScript|javascript|Javascript', na=False)]
count_javascript_lines = len(javascript_lines)

# Count the number of lines containing 'Java' but not 'JavaScript'
java_lines = df[df['title'].str.contains('Java', na=False) & ~df['title'].str.contains('JavaScript', na=False)]
count_java_lines = len(java_lines)

# Print the results
print(f'a) Count of lines containing python or Python: {count_python_lines}')
print(f'b) Count of lines containing JavaScript, javascript, or Javascript: {count_javascript_lines}')
print(f'c) Count of lines containing Java and not JavaScript: {count_java_lines}')

