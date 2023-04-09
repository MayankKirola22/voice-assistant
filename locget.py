from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="maps")
location = geolocator.reverse("29.3433166,79.5651877")
print(location.address)
