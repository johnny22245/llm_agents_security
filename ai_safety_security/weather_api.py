import requests
import traceback
import json

"""
getting api keys
"""

def get_file_contents(filename):
    """ Given a filename,
        return the contents of that file
    """
    try:
        with open(filename, 'r') as f:
            # It's assumed our file contains a single line,
            # with our API key
            return f.read().strip()
    except FileNotFoundError:
        print("'%s' file not found" % filename)

# WeatherAgent - Fetch weather information from an API
class WeatherAgent:
    def __init__(self):
        api_key = get_file_contents('weather_api_key.key')
        api_geo_key = get_file_contents("geo_api_key.key")
        self.api_key = api_key
        self.api_geo_key = api_geo_key
        self.base_url = "https://api.meteoblue.com/weather"

    def get_weather(self, city: str):
        """
        Fetches the current weather data for a given city using the Meteoblue API.

        Args:
            api_key (str): Your Meteoblue API key.
            city (str): The city name to fetch weather data for.

        Returns:
            dict: A dictionary containing weather details like temperature, humidity, wind, and condition.
        """
        def get_geo_code(city, api_geo_key):
            try:
                city_q = "%20".join(city.lower().split())
                geo_url = f"https://geocode.maps.co/search?q={city_q}&api_key={api_geo_key}"
                result_ = requests.get(geo_url)
                result = json.loads(result_.content)
                lat_lang = {"latitude": result[0]["lat"], "longitude": result[0]["lon"]}
                return lat_lang
            except:
                err = str(traceback.format_exc())
                return {"error": err}
        
        try:
            lat_lon_result = get_geo_code(city, self.api_geo_key)
            if "error" in lat_lon_result:
                return {"error": "Error in fetching latitude & longitude."}
            else:
                lat, lon = lat_lon_result["latitude"], lat_lon_result["longitude"]
            # Meteoblue endpoint for the weather data
            base_url = "https://my.meteoblue.com/packages/basic-day"
            params = {
                "apikey": self.api_key,    # Your API key
                "lat": lat,         # latitude
                "lon": lon,         # longitude
                "format": "json"      # Response format
            }

            # Make the API request
            response = requests.get(base_url, params=params)

            if response.status_code != 200:
                return {"error": f"API Request Failed: {response.status_code}, {response.text}"}

            # Parse the JSON response
            data = response.json()
            #print(data)
            # Extract relevant weather data
            weather_info = {
                "City": city,
                "Temperature": f"{data['data_day']['temperature_mean'][0]}°C",
                "Humidity": f"{data['data_day']['relativehumidity_mean'][0]}%",
                "Wind": f"{data['data_day']['windspeed_mean'][0]} km/h",
                "Condition": data['data_day']['pictocode'][0]
            }

            return weather_info

        except Exception as e:
            return {"error": str(e)}


