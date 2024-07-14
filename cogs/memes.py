import discord
from discord.ext import commands
from tools import openai_request, get_lat_lon, open_meteo_request, meme_template


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="wetter", description="Generate a Weather meme")
    async def meme(self, ctx, location: str):
        lat, lon = await get_lat_lon.get_coordinates(location)
        data = await open_meteo_request.get_all_weather_data(lat, lon)
        template = await meme_template.get_template()
        image_url = await openai_request.call_openai(location, data, template)
        ctx.respond("hehe", file=image_url)
