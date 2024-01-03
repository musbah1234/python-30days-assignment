'''
import requests
from bs4 import BeautifulSoup
import json

# URL of the website
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant information from the webpage
    # (Replace this part with your specific scraping requirements)
    data_to_scrape = {
        "title": soup.title.text,
        "paragraphs": [p.text.strip() for p in soup.find_all('p')]
        # Add more data extraction as needed
    }

    # Store the scraped data as a JSON file
    with open('scraped_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data_to_scrape, json_file, ensure_ascii=False, indent=2)

    print('Data scraped and stored successfully as "scraped_data.json".')
else:
    print(f'Error: Unable to fetch data. Status code: {response.status_code}')
    
    

    import requests
from bs4 import BeautifulSoup
import json

# URL of the website containing the table
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table element
    table = soup.find('table')

    # Extract table data
    table_data = []
    for row in table.find_all('tr'):
        row_data = [col.text.strip() for col in row.find_all(['th', 'td'])]
        table_data.append(row_data)

    # Remove empty rows
    table_data = [row for row in table_data if row]

    # Convert the table data to a JSON format
    json_data = json.dumps(table_data, ensure_ascii=False, indent=2)

    # Save the JSON data to a file
    with open('table_data.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_data)

    print('Table data extracted and saved as "table_data.json".')
else:
    print(f'Error: Unable to fetch data. Status code: {response.status_code}')


'''
import pandas as pd

# Wikipedia URL containing the Presidents table
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'

# Read HTML tables from the URL
tables = pd.read_html(url, match='Presidency')

# Assuming the Presidents table is the first table on the page
presidents_table = tables[0]

# Convert the DataFrame to a JSON file
presidents_table.to_json('presidents_data.json', orient='records', lines=True)

print('Presidents data extracted and saved as "presidents_data.json".')

