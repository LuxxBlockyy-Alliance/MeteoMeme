import json
import os
import asyncio
import random

import requests
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ.get("OPENAI_KEY"),
)


async def call_openai(stadt, wetter, random_template):
    sys_prompt = ("Du bist ein Meme-Ideengenerator. Du verwendest die Memegen-API, um ein Meme zu erstellen, "
                  "das auf humorvolle Weise das Wetter darstellt. Generiere eine Meme-Idee basierend auf einer "
                  "zufälligen Vorlage und verschiedenen Wetterbedingungen wie Sonne, Regen, Schnee oder Hitze. Das "
                  "Meme soll die typischen Reaktionen auf das Wetter oder lustige Situationen, die durch das Wetter "
                  "entstehen, darstellen. Verwende dafür nur die bereitgestellte Vorlage. Bitte auch alles auf "
                  "Deutsch! Außerdem bitte auch keine Sonderzeichen, wie Ö,Ä,Ü, sondern ersetz sie mit oe, ae, ue "
                  "Außerdem bitte ersetz alle Leerzeichen mit einem Unterstrich")
    user_prompt = f"Stadt: {stadt} \n\n Wetter: {wetter} \n\n Template: {random_template['name']} \n"

    try:
        response = await client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=[
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": user_prompt}
            ],
            functions=[
                {
                    "name": "generateMemeImage",
                    "description": "Generiere Memes über die Memegen-API basierend auf dem Wetter",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "text0": {"type": "string", "description": "Der Text für die obere Überschrift des Memes"},
                            "text1": {"type": "string", "description": "Der Text für die untere Überschrift des Memes"}
                        },
                        "required": ["templateName", "text0", "text1"]
                    }
                }
            ],
            function_call={"name": "generateMemeImage"}
        )
    except Exception as e:
        print('Error calling OpenAI: ', e)
        raise Exception('Error calling OpenAI')

    if not response.choices[0].message.function_call:
        raise Exception('No function call in OpenAI response')

    gpt_args = json.loads(response.choices[0].message.function_call.arguments)
    print('gptArgs: ', gpt_args)

    return f"https://api.memegen.link/images/{random_template['id']}/{gpt_args['text0']}/{gpt_args['text1']}.png".replace(" ", "_")


