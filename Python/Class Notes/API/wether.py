import requests

base_url = "https://api.weather.gov/points/"

def get_forecast(latitude, longitude):
    url = f"{base_url}{latitude},{longitude}"
    response = requests.get(url)
    print(response)  # shows status code
    data = response.json()
    print(data)
get_forecast(39.7456, -97.0892)

