from open_meteo import OpenMeteo
from open_meteo.models import HourlyParameters


async def get_current_weather(latitude, longitude):
    async with OpenMeteo() as open_meteo:
        try:
            forecast = await open_meteo.forecast(
                latitude=latitude,
                longitude=longitude,
                current_weather=True,
                hourly=[
                    HourlyParameters.TEMPERATURE_2M,
                    HourlyParameters.WEATHER_CODE,
                    HourlyParameters.WIND_SPEED_10M,
                    HourlyParameters.WIND_DIRECTION_10M,
                    HourlyParameters.RELATIVE_HUMIDITY_2M,
                    HourlyParameters.PRECIPITATION,
                ],
            )
            return forecast
        except Exception as e:
            print(f"Error fetching weather data: {e}")
            return None


async def get_all_weather_data(lat, lon):
    weather_data = await get_current_weather(lat, lon)
    if weather_data:
        # Zugriff auf die Wetterdaten
        temperature = weather_data.hourly.temperature_2m
        weather_code = weather_data.hourly.weather_code
        wind_speed = weather_data.hourly.wind_speed_10m
        wind_direction = weather_data.hourly.wind_direction_10m
        humidity = weather_data.hourly.relative_humidity_2m
        precipitation = weather_data.hourly.precipitation

        output = (
            f"Aktuelles Wetter in den Koordinaten ({lat}, {lon}):\n"
            f"Temperatur: {temperature[0]} °C\n"
            f"Wettercode: {weather_code[0]}\n"
            f"Windgeschwindigkeit: {wind_speed[0]} m/s\n"
            f"Windrichtung: {wind_direction[0]} °\n"
            f"Luftfeuchtigkeit: {humidity[0]} %\n"
            f"Niederschlag: {precipitation[0]} mm"
        )

        print(output)
        return output
    else:
        raise Exception("No weather data available")

