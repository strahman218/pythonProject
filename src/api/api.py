import requests
from static import google_maps_api_data as g
from math import sin, cos, sqrt, atan2, radians


def get_location_data(location=None, location2=None, speed=3.5):
    result = {}

    # geodata: {address, lat, lng}
    geodata = get_geodata(location)
    geodata2 = get_geodata(location2)

    if geodata and geodata2:
        # set locations and latitudes and longitudes
        result['location1'] = geodata['address']
        result['location2'] = geodata2['address']
        result['lat'] = geodata['lat']
        result['lng'] = geodata['lng']
        result['lat2'] = geodata['lat']
        result['lng2'] = geodata['lng']

        # distance in miles
        distance = get_distance(geodata, geodata2)
        result['distance'] = format(distance, '.2f')

        # get the number of hours it would take @ speed to reach distance
        miles_per_hour = format(float(result['distance'])/float(speed), '.2f')
        time = get_time(miles_per_hour)

        result['hour'] = time['hour']
        result['minutes'] = time['minutes']
        return result
    else:
        print("get_location_data: Some geodata is missing!")
        return result


def get_time(time=None):
    # null check
    if time is None:
        return None

    # if time isn't a string, format it
    if type(time) is not str:
        time = repr(time)

    time_dict = {}

    # convert float to string, split on decimal to get hours and minutes
    split_time = time.split('.')
    get_hour = int(float(split_time[0]))

    #if the time we get is 2.5, format it to 2.50
    if len(split_time[1]) == 1:
        split_time[1] += '0'

    get_minutes = round(float(split_time[1])/100 * 60)

    # check if hours and minutes are in bounds
    if get_hour < 0 or get_minutes > 60 or get_minutes < 0:
        return None

    time_dict['hour'] = get_hour
    time_dict['minutes'] = get_minutes
    return time_dict


def get_geodata(location=None):
    if type(location) is str:
        param_type = get_location_type(location)
        params = {
            param_type: location,
            'key': g.token
        }

        req = requests.get(g.base_url, params=params)
        res = req.json()
        print(res['results'])

        if len(res['results']) > 0:
            result = res['results'][0]

            geodata = dict()
            geodata['lat'] = result['geometry']['location']['lat']
            geodata['lng'] = result['geometry']['location']['lng']
            geodata['address'] = result['formatted_address']
            return geodata
        else:
            print("get_geodata: No results for this location!")
            return None
    else:
        print("get_geodata: Location needs to be a string!")


def get_location_type(location=None):
    if type(location) is str:
        parse_loc = location.split(",")
        if len(parse_loc) == 2:
            try:
                float(parse_loc[0])
                float(parse_loc[1])
                return 'latlng'
            except ValueError:
                return 'address'
        else :
            return 'address'
    else:
        print("get_location_type: Invalid location format")


def get_distance(location1, location2):
    is_valid = check_valid_location(location1, location2)

    if is_valid is True:
        origin_lat = radians(float(location1['lat']))
        origin_lng = radians(float(location1['lng']))
        dest_lat = radians(float(location2['lat']))
        dest_lng = radians(float(location2['lng']))

        # approximate radius of earth in km
        R = 6373.0

        #1 km = 0.62 miles
        k_to_miles = 0.621371

        dlng = dest_lng - origin_lng
        dlat = dest_lat - origin_lat

        a = sin(dlat / 2) ** 2 + cos(origin_lat) * cos(dest_lat) * sin(dlng / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return float(R * c * k_to_miles)
    else:
        print("get_distance: Missing one or both locations. Please enter a location!")
        return None


def check_valid_location(location1, location2):
    print("check valid location!")
    if location1 is None or location2 is None or not location1 or not location2:
        print("check_valid_location: Missing either one or both locations!")
        return False
    elif type(location1) is not dict or type(location2) is not dict:
        print("check_valid_location: Invalid location formatting")
        return False
    elif location1['lat'] is None or location1['lng'] is None:
        print('check_valid_location: Missing latitude/longitude for location1')
        return False
    elif location2['lat'] is None or location2['lng'] is None:
        print("check_valid_location: Missing latitude/longitude for location2")
        return False
    else:
        try:
            float(location1['lat'])
            float(location2['lng'])
            float(location2['lat'])
            float(location2['lng'])

            print(type(location1['lat']))
            valid_bounds1 = check_valid_bounds(location1['lat'], location1['lng'])
            valid_bounds2 = check_valid_bounds(location2['lat'], location2['lng'])

            print("check valid bounds!!")
            print(valid_bounds2)
            print(valid_bounds1)
            if valid_bounds1 and valid_bounds2:
                return True
            else:
                return False
        except ValueError:
            print("not a float y'all")
            return False


def check_valid_bounds(latitude, longitude):
    if latitude is not None and longitude is not None:
        try:
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            print("tried to convert to float, didn't work")
            return False

    if type(latitude) is float and type(longitude) is float:
        if longitude >= 180.00 or longitude <= -180.00:
            print("longitude is out of bounds!")
            return False
        elif latitude >= 90.00 or latitude <= -90.00:
            print("latitude out of bounds!")
            return False
        else:
            return True
    else:
        return False
