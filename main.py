import requests
from selenium import webdriver
import folium
import datetime
import time

from geopy.gecoders import Nominatim

def get_gps_coordinates(address):
    geolocator

def locationCoordinates():
    try:
        response = requests.get('https://ipinfo.io')
        data = response.json()
        loc = data['loc'].split(',')
        lat, long = float(loc[0]), float(loc[1])
        city = data.get('city', 'Unknown City')
        state = data.get('region', 'Unknown Region')
        return lat, long, city, state
        #return lat, long
    except:
        print("You are not connected to the internet")
        #exit()
        return False
    
def gps_locator():
    obj = folium.Map(location=[0, 0], zoom_start=2)

    try:
        lat, long, city, state = locationCoordinates()
        print("You are in {},{}".format(city, state))
        print("Your latitude = {} and longitude = {}".format(lat, long))
        folium.Marker([lat, long], popup='Current Location').add_to(obj)

        fileName = "C:/Users/eddz9/Desktop/LoConnected/Location" + str(datetime.date.today()) + ".html"
        
        obj.save(fileName)
        return fileName

    except:
        print("You are not connected to the internet.")
        #exit()
        return False
    
if __name__ == "__main__":
    print("---------------GPS Using Python---------------\n")
    # function Calling
    page = gps_locator()
    print("\nOpening File.............")
    dr = webdriver.Chrome()
    dr.get(page)
    time.sleep(4)
    dr.quit()
    print("\nBrowser Closed..............")