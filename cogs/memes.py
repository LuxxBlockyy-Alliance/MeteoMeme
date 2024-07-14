import asyncio

import discord
import requests
from discord.ext import commands
from tools import openai_request, get_lat_lon, open_meteo_request


class Memes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="wetter", description="Generate a Weather meme")
    async def meme(self, ctx, location: str):
        embed = discord.Embed(title="Wetter Meme wird generiert...", description="📍 Koordinaten werden geladen... 📍",
                              colour=discord.Color.blue())
        interaction = await ctx.respond(embed=embed)
        message = interaction.message
        await interaction.edit(embed=embed)
        lat, lon = await get_lat_lon.get_coordinates(location)
        await asyncio.sleep(1.5)
        embed = discord.Embed(title="Wetter Meme wird generiert...", description="🔗 Open Meteo API wird abgefragt... 🔗",
                              colour=discord.Color.blue())
        await interaction.edit(embed=embed)
        data = await open_meteo_request.get_all_weather_data(lat, lon)
        await asyncio.sleep(1.5)
        embed = discord.Embed(title="Wetter Meme wird generiert...", description="🛠️ Wetter Meme Url wird erstellt...🛠️",
                              colour=discord.Color.blue())
        await interaction.edit(embed=embed)
        image_url = await openai_request.call_openai(location, data)
        while requests.get(image_url).status_code == 500:
            image_url = await openai_request.call_openai(location, data)
        embed = discord.Embed(title="⛅ MeteoMeme ⛅", description="`developed by Luxx & Janosch`", colour=discord.Color.blue())
        embed.set_image(url=image_url)
        await interaction.edit(embed=embed)
        await asyncio.sleep(0.5)
        message = await ctx.fetch_message(interaction.id)
        print(message.content)
        await message.add_reaction('\N{THUMBS UP SIGN}')
        await message.add_reaction('\N{THUMBS DOWN SIGN}')



def setup(bot):
    bot.add_cog(Memes(bot))
