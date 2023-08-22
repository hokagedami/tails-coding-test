from geopy.distance import geodesic

from helpers import geolocation


def get_stores_in_postcode_radius(postcode, radius, stores_data):
    stores = []
    if (type(radius) != int and type(radius) != float) or type(postcode) != str or type(stores_data) != list:
        return stores
    for store in stores_data:
        if store['latitude'] == "Not Available" or store['longitude'] == "Not Available":
            continue

        lat, long = (store['latitude'], store['longitude']) if store['postcode'] == postcode \
            else geolocation.get_geolocation(postcode)
        distance = geodesic((store['latitude'], store['longitude']),
                            (lat, long)).kilometers
        if distance <= radius:
            store['distance'] = distance
            stores.append(store)
    stores.sort(key=lambda x: x['distance'])
    return stores
