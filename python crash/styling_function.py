# make_shirt function
def make_shirt(size, text):
    print(f"This shirt is size {size} and {text} is printed on it")

make_shirt(80, "chosen one")
make_shirt(size=70, text="I am Invincible")

# describe_city funtion

def describe_city(city, country="Nigeria"):
    print(f"{city.capitalize()} is in {country.capitalize()}")

describe_city("acra", "Ghana")
describe_city("tokyo", "Japan")
describe_city("abuja")

# make_album function

def make_album(artist, title, songs=None):
    album_info = {'artist': artist, 'title': title}
    if songs is not None:
        album_info['songs'] = songs
    return album_info

# Creating three dictionaries representing different albums
album1 = make_album('Adele', '21')
album2 = make_album('Ed Sheeran', '÷', 12)
album3 = make_album('Taylor Swift', 'Red', 16)

# Printing each return value to show the stored album information
print(album1)
print(album2)
print(album3)


