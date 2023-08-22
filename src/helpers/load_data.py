from helpers import geolocation
import json


def load_store_data():
    # Load stores data from JSON file
    try:
        with open('stores.json') as f:
            data = json.load(f)
        print("Stores data loading, please wait...")
        stores_data = sorted(data, key=lambda x: x['name'])
        for i, store in enumerate(stores_data, start=1):
            response = geolocation.get_geolocation(store['postcode'])
            if all(element is None for element in response):
                store['latitude'], store['longitude'] = "Not Available", "Not Available"
            else:
                store['latitude'], store['longitude'] = response
            store['index'] = i
        print("Stores loading complete!")
        return stores_data
    except Exception as e:
        print(f"Error!:::{e}")
        return []
