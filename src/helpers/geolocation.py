import requests

GEOLOCATION_API_URL = "https://api.postcodes.io/postcodes/{}"


def get_geolocation(postcode):
    response = requests.get(GEOLOCATION_API_URL.format(postcode))
    data = response.json()
    if response.status_code == 200:
        return data['result']['latitude'], data['result']['longitude']
    return None, None
