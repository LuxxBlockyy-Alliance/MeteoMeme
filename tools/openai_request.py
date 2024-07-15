import json
import os
import configparser
from openai import AsyncOpenAI

config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['KEYS']['openai_key']

client = AsyncOpenAI(
    api_key=api_key
)


async def call_openai(location, wetter):

    with open('prompt.txt', 'r') as prompt:
        sys_prompt = prompt.read()

    user_prompt = f"Stadt: {location} \n\n Wetter: {wetter}\n"

    try:
        chat_completion = await client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
    except Exception as e:
        print('Error calling OpenAI: ', e)
        raise Exception('Error calling OpenAI')

    if not chat_completion.choices[0].message:
        raise Exception('No function call in OpenAI response')

    response = chat_completion.choices[0].message.content.replace(" ", "+")
    print(response)
    return response


