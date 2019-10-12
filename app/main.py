#!/usr/bin/env python3

import datetime
from geopy.geocoders import Nominatim
import astral

__author__ = "Ioannis Katsikavelas"
__copyright__ = "2019"
__version__ = "0.0.1"
__description__ = "IoT Cancas. Light up your Artworks"


def error(error: str):
    ''' 
    Exit with an error message
    
    :param error: the error message string
    :return: nothing
    '''
    print(error)
    sys.exit(2)

def get_Location_times(location)

if __name__ == '__main__':

    geolocator = Nominatim()
    city = 'Larissa'
    country = "Greece"
    loc = geolocator.geocode(city+','+country)
    print("\nCity: %s | Country: %s"%(city, country))
    print("\nlatitude is : " ,loc.latitude,"\nlongtitude is: " ,loc.longitude)


    loc = astral.Location((city, country, loc.latitude, loc.longitude, 'Europe/Athens', 510))

    dawn = loc.sun(datetime.date.today())['dawn']
    dusk = loc.sun(datetime.date.today())['dusk']


