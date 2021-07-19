import os
from pyowm import OWM

if __name__ == "__main__":
    API_KEY = os.getenv("OPENWEATHER_API_KEY")
    CITY_NAME = os.getenv("CITY_NAME")
    owm = OWM(API_KEY) 
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(CITY_NAME)
    weather = observation.weather
    print(f'source=openweathermap city={CITY_NAME} description={weather.detailed_status} temp={weather.temperature("celsius").get("temp")} humidity={weather.humidity}')