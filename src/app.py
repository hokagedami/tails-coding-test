from flask import Flask, render_template, request, jsonify
import requests_cache

from helpers import load_data as loader, radius_finder as finder

app = Flask(__name__)
requests_cache.install_cache('stores_api_cache', backend='sqlite', expire_after=2)
stores_data = loader.load_store_data()  # Load stores data before server starts


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/stores_in_radius', methods=['GET'])
def stores_in_radius():
    postcode = request.args.get('postcode')
    radius = float(request.args.get('radius', 10))  # Radius default to 10km

    stores_result = finder.get_stores_in_postcode_radius(postcode, radius, stores_data)
    return jsonify(stores_result)


@app.route('/stores')
def index():
    return render_template('index.html', stores=stores_data)


if __name__ == '__main__':  # Load stores data before server starts
    app.run(debug=True)
