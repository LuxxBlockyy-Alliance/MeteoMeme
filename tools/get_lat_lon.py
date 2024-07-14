import requests


async def get_coordinates(location):
    url = f"https://nominatim.openstreetmap.org/search?q={location}&format=json&addressdetails=1&limit=1&polygon_svg=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if data:
            lat = float(data[0]["lat"])
            lon = float(data[0]["lon"])
            return [lat, lon]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Fehler: {e}")
        return None
