# Initialize Nominatim API

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="MyApp")

location = geolocator.geocode("Hyderabad")

print("The latitude of the location is: ", location.latitude)
print("The longitude of the location is: ", location.longitude)