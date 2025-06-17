from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/country')
def get_country_info():
    name = request.args.get('name')
    if not name:
        return jsonify({'error': 'Missing country name'}), 400

    response = requests.get(f"https://restcountries.com/v3.1/name/{name}")
    if response.status_code != 200:
        return jsonify({'error': 'Country not found'}), 404

    data = response.json()[0]
    result = {
        'name': data.get('name', {}).get('common'),
        'capital': data.get('capital', [None])[0],
        'region': data.get('region'),
        'population': data.get('population'),
        'area': data.get('area'),
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
