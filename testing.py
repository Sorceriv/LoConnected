from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="LoConnected")

while True:
    location = geolocator.geocode("Your location")
    print(location.address)
    time.sleep(5)  # Print location every 5 seconds