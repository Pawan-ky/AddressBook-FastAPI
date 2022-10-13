from geopy.geocoders import Nominatim

def get_coodinates(address):
    
    geolocator = Nominatim(user_agent="app")
    location = geolocator.geocode(address)
    if location is None:
        return "NA", "NA"

    return str(location.latitude),str(location.longitude)
