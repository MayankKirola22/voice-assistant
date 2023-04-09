from selenium import webdriver
from geopy.geocoders import Nominatim
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import reverse_geocoder as rg 
import pprint 
import time
def getLocation():
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = "C:\Program Files (x86)\ChromeDriver\chromedriver.exe", options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(1)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    return(latitude,longitude)
    
def addr(coor):
    geolocator = Nominatim(user_agent="maps")
    location = geolocator.reverse(coor)
    p=location.address.split(',')
    x=[p[0],p[-4],p[-3],p[-1]]
    return x

def trueloc():
    p=getLocation()
    coordinates =(p[0],p[1]) 
    l=addr(coordinates)
    return l
