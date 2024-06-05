import pyowm

owm = pyowm.OWM('c548bc34f606696689b7c67ce8cbdbc7')

city = "London"
mgr= owm.weather_manager()
observation =mgr.weather_at_place(city)
weather=observation.weather

print(f"weather in {city}: ")
print(f"Status: {weather.detailed_status}")
print(f"Temperature: {weather.temperature('celsius')['temp']}°C")
print(f"Humidity: {weather.humidity}%")
print(f"Wind Speed: {weather.wind()['speed']} m/s")