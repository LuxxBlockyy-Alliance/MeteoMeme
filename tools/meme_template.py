import aiohttp
import asyncio
import random


async def fetch_template(session):
    async with session.get("https://api.memegen.link/templates/") as response:
        return await response.json()


async def get_template():
    async with aiohttp.ClientSession() as session:
        data = await fetch_template(session)
        return random.choice(data)


