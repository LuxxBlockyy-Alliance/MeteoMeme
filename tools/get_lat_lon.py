from open_meteo import OpenMeteo


async def get_coordinates(location):
    async with OpenMeteo() as open_meteo:
        search = await open_meteo.geocoding(
            name=location,
        )
        data = search.to_dict()
        if data:
            results = data['results'][0]
            lat = float(results['latitude'])
            lon = float(results['longitude'])
            return [lat, lon]
        else:
            raise Exception(f"No data for {location} found!")

