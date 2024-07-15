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
        await interaction.edit(embed=embed)
        try:
            lat, lon = await get_lat_lon.get_coordinates(location)
        except:
            embed = discord.Embed(title="Tja, ein Fehler",
                                  description="Hast du versucht mehr, als nur ein Wort zu nutzen?",
                                  colour=discord.Color.red())
            await interaction.edit(embed=embed)
            return
        await asyncio.sleep(1.5)
        embed = discord.Embed(title="Wetter Meme wird generiert...",
                              description="🔗 Open Meteo API wird abgefragt... 🔗",
                              colour=discord.Color.blue())
        await interaction.edit(embed=embed)
        data = await open_meteo_request.get_all_weather_data(lat, lon)
        await asyncio.sleep(1)
        embed = discord.Embed(title="Wetter Meme wird generiert...",
                              description="🛠️ Wetter Meme Url wird erstellt...🛠️",
                              colour=discord.Color.blue())
        await interaction.edit(embed=embed)
        image_url = await openai_request.call_openai(location, data)
        while requests.get(image_url).status_code == 500:
            image_url = await openai_request.call_openai(location, data)
        embed = discord.Embed(title="⛅ MeteoMeme ⛅", description="`developed by Luxx & Janosch`",
                              colour=discord.Color.blue())
        embed.set_image(url=image_url)
        await interaction.edit(embed=embed)
        message = await interaction.original_response()
        await message.add_reaction("👍")
        await message.add_reaction("👎")
        await asyncio.sleep(0.5)


def setup(bot):
    bot.add_cog(Memes(bot))
