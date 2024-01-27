import requests
import logging
import csv
from io import StringIO

logging.basicConfig(level=logging.INFO)

url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv' 

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info('Successfully fetched the movie data.')
        movie_data = response.content.decode('utf-8')

        # Use StringIO to treat the string as a file for csv.reader
        csv_reader = csv.reader(StringIO(movie_data))

        # Skip the header row
        header = next(csv_reader)

        for row in csv_reader:
            # Check for non-empty rows
            if row:
                # Each row is a tuple representing a movie
                movie_tuple = tuple(row)
                print(movie_tuple)
                # Now you can access data like movie_tuple[0] for title, movie_tuple[1] for year, etc.

    else:
        logging.error(f'Failed to fetch data. Status code: {response.status_code}')

except requests.RequestException as e:
    logging.error(f'Failed to fetch data. Error: {e}')


import csv
import logging

# Setup logging
logging.basicConfig(level=logging.DEBUG) 

# File path for 'IMDB-Movie-Data.csv' 
file_path = 'movies.csv'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        # Skip the header row if present
        next(reader, None)

        # Process each row as a tuple
        for row in reader:
            # Each 'row' is a tuple representing a movie
            movie_tuple = tuple(row)

            # Unpack the tuple
            # Adjust the number of variables based on number of columns in CSV
            # Ensure CSV file has these columns, in the correct order
            title, year, genre, director, rating = movie_tuple

            # Log each unpacked item
            logging.debug(f"Title: {title}")
            logging.debug(f"Year: {year}")
            logging.debug(f"Genre: {genre}")
            logging.debug(f"Director: {director}")
            logging.debug(f"Rating: {rating}")

except FileNotFoundError:
    logging.error(f"File not found: {file_path}")
except Exception as e:
    logging.error(f"Error occurred: {e}")


    {
  "location": {
    "city": "San Francisco",
    "country": "USA",
    "coordinates": {"latitude": 37.7749, "longitude": -122.4194}
  },
  "weather": {
    "temperature": 15,
    "humidity": 72,
    "condition": "Cloudy",
    "wind_speed": 5.2,
    "wind_direction": "NW"
  },
  "forecast": [
    {"day": "Monday", "high": 17, "low": 12, "condition": "Partly Cloudy"},
    {"day": "Tuesday", "high": 19, "low": 13, "condition": "Sunny"},
    {"day": "Wednesday", "high": 18, "low": 14, "condition": "Rain"},
    {"day": "Thursday", "high": 16, "low": 11, "condition": "Fog"},
    {"day": "Friday", "high": 15, "low": 10, "condition": "Windy"}
  ]
}
    import requests
import logging
import csv
from io import StringIO

logging.basicConfig(level=logging.INFO)

url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv' 

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info('Successfully fetched the movie data.')
        movie_data = response.content.decode('utf-8')

        # Use StringIO to treat the string as a file for csv.reader
        csv_reader = csv.reader(StringIO(movie_data))

        # Skip the header row
        header = next(csv_reader)

        # Process each row as a tuple
        for row in csv_reader:
            # Check for non-empty rows
            if row:
                # Each row is a tuple representing a movie
                movie_tuple = tuple(row)
                print(movie_tuple)
                # Now you can access data like movie_tuple[0] for title, movie_tuple[1] for year, etc.

        # Processing text data
        words = ' '.join(row[0] for row in csv_reader).split()
        unique_words = set(words)

        # Word count using list comprehension and dictionary
        word_count = {word: words.count(word) for word in unique_words}

        logging.info(word_count)

    else:
        logging.error(f'Failed to fetch data. Status code: {response.status_code}')

except requests.RequestException as e:
    logging.error(f'Failed to fetch data. Error: {e}')
except Exception as e:
    logging.error(f'Error occurred: {e}')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()
import requests
import logging
import csv
from io import StringIO

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv' 

try:
    response = requests.get(url)
    
    if response.status_code == 200:
        logging.info('Successfully fetched the movie data.')
        movie_data = response.content.decode('utf-8')

        # Use StringIO to treat the string as a file for csv.reader
        csv_reader = csv.reader(StringIO(movie_data))

        # Skip the header row
        header = next(csv_reader)

        # Process each row as a tuple
        for row in csv_reader:
            # Check for non-empty rows
            if row:
                # Each row is a tuple representing a movie
                movie_tuple = tuple(row)
                print(movie_tuple)
                # Now you can access data like movie_tuple[0] for title, movie_tuple[1] for year, etc.

        # Processing text data
        words = ' '.join(row[0] for row in csv_reader).split()
        unique_words = set(words)

        # Word count using list comprehension and dictionary
        word_count = {word: words.count(word) for word in unique_words}

        logging.info(word_count)

    else:
        logging.error(f'Failed to fetch data. Status code: {response.status_code}')

except requests.RequestException as e:
    logging.error(f'Failed to fetch data. Error: {e}')
except Exception as e:
    logging.error(f'Error occurred: {e}')


    # Word count using list comprehension and dictionary
word_count = {word: words.count(word) for word in unique_words}

logger.info(word_count )

# Optional: Sorting the dictionary by count using a dict
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

# Display the result
print(sorted_word_count)

import requests
import json

def fetch_weather_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
    import json

def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

# Example usage:
data_to_save = {'key': 'value', 'another_key': 42}
save_json(data_to_save, 'output.json')


        
def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)
    
    import json

import json

def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def read_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None

# Example usage:
filename = 'example.json'
data = read_json(filename)
print(data)

import json
import requests

def fetch_weather_data(api_url):
    # Assume this function fetches weather data from the specified API
    # and returns the data as a dictionary
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")
        return None

def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def read_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

# URL of the weather API
api_url = 'https://api.example.com/weather'

# Fetch the weather data
weather_data = fetch_weather_data(api_url)

if weather_data:
    # Save the data to a file
    save_json(weather_data, 'weather_data.json')

    # Read the data back into a dictionary
    saved_weather_data = read_json('weather_data.json')

    # Use the data
    print(saved_weather_data)
def read_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return None
    
    
# URL of the weather API
api_url = 'https://api.example.com/weather'

# Fetch the weather data
weather_data = fetch_weather_data(api_url)

if weather_data:
    # Save the data to a file
    save_json(weather_data, 'weather_data.json')

    # Read the data back into a dictionary
    saved_weather_data = read_json('weather_data.json')

    # Use the data
    print(saved_weather_data)



