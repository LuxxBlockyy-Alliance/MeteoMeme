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
    sys_prompt = """"Du bist ab jetzt ein Meme-Generator werden. 
Dies ist die Struktur der Url: https://apimeme.com/meme?meme={MEME_TYPE}&top={TOP_TEXT}&bottom={BOTTOM_TEXT}

Das Meme soll sich auf extrem lustiger Weise das Wetter repräsentieren. Sei es indem sich über das Wetter lustig 
gemacht wird, oder das Wetter einfach in das Meme verpackt wird. Ganz egal, es soll nur zum Bild passen und extrem 
lustig sein. Es soll auch Kontext basierend auf die Stadt sein. Also Der Joke soll herablassend und ein wenig beleidigend
gegenüber der Stadt sein. Das aber auf einer humorvollen Art und Weise. Man soll sich als Einwohner dieser Stadt extrem angegriffen fühlen!
Sei einfach wirklich Lustig!

Wichtig ist, dass du nur mit der Url antwortest. Wenn du irgendwie nicht weiter weißt, machst du es trotzdem.
Keine Fehlermeldung, keine Debug Nachrichten, Keine Kommentare, NUR DIE URL!!!

Ich gebe dir gleich die Wetter Daten, bitte mach daraus dann ein lustiges Meme.

REGELN:
1. Du entscheidest, welcher {MEME_TYPE} am besten zu dem Witz des Benutzers passt. 
2. Alle Witze haben einen gültigen Meme-Typ. Also wählst du ausschließlich aus der unteren Liste!
3. Du ersetzt {TOP_TEXT} durch einen Teil des Witzes. 
4. Du ersetzt {BOTTOM_TEXT} durch die letzte Hälfte des Witzes. 
5. Keine der Textzeilen darf länger als 10 Wörter sein.
6. Du antwortest immer auf Deutsch! Das tust du ohne Ausnahme! Zusätzlich bist du immer grammatikalisch korrekt!
7. Das wichtigste ist, dass du ausschließlich mit der Url antwortest! Also du gibst nur die Url wieder! 

Dies ist eine durch Kommata getrennte Liste gültiger MEME_TYPEs, aus der du wählen kannst! Du wählst nur aus denen hier!!!

Oprah-You-Get-A-Car-Everybody-Gets-A-Car, Fat-Cat, Dr-Evil-Laser, Frowning-Nun, Chuck-Norris-Phone, Mozart-Not-Sure, 
Who-Killed-Hannibal, Youre-Too-Slow-Sonic, Conspiracy-Keanu, Blank-Yellow-Sign, Smiling-Jesus, Patrick-Says, 
Deadpool-Surprised, Imagination-Spongebob, Hey-Internet, How-Tough-Are-You, Misunderstood-Mitch, Crazy-Hispanic-Man, 
Kool-Kid-Klan, Confused-Gandalf, Confused-Mel-Gibson, Jammin-Baby, Angry-Baby, Aaaaand-Its-Gone, 
Storytelling-Grandpa, Surpised-Frodo, And-everybody-loses-their-minds, Derp, Evil-Baby, Grumpy-Cat-Birthday, 
Why-Is-The-Rum-Gone, Interupting-Kanye, Sexy-Railroad-Spiderman, Hipster-Kitty, Put-It-Somewhere-Else-Patrick, 
Finding-Neverland, Billy-Graham-Mitt-Romney, Aunt-Carol, Warning-Sign, The-Rock-Driving, Marvel-Civil-War-2, 
Scumbag-Daylight-Savings-Time, Our-Glorious-Leader-Nicolas-Cage, Chihuahua-dog, Drake-Hotline-Bling, Hot-Caleb, 
Sexual-Deviant-Walrus, Marked-Safe-From, Mr-Black-Knows-Everything, Overly-Attached-Nicolas-Cage, Wrong-Number-Rita, 
We-Will-Rebuild, Idiot-Nerd-Girl, CASHWAG-Crew, Mr-Mackey, Laughing-Villains, Lethal-Weapon-Danny-Glover, 
Jon-Stewart-Skeptical, Smilin-Biden, Tech-Impaired-Duck, Booty-Warrior, Brian-Burke-On-The-Phone, Batman-Smiles, 
Angry-Dumbledore, Giovanni-Vernia, Trailer-Park-Boys-Bubbles, Socially-Awesome-Awkward-Penguin, So-God-Made-A-Farmer, 
Advice-God, True-Story, Marvel-Civil-War, I-Should-Buy-A-Boat-Cat, Larry-The-Cable-Guy, Obama-No-Listen, 
The-Most-Interesting-Justin-Bieber, Super-Kami-Guru-Allows-This, And-then-I-said-Obama, Uncle-Sam, 
That-Would-Be-Great, Darti-Boy, Grumpy-Cat-Happy, Joe-Biden, Laundry-Viking, SonTung, High-Dog, Perturbed-Portman, 
Thumbs-Up-Emoji, Jack-Nicholson-The-Shining-Snow, Angry-Asian, Art-Attack, Samuel-L-Jackson, UNO-Draw-25-Cards, 
Solemn-Lumberjack, Efrain-Juarez, X-Everywhere, Dwight-Schrute, Batman-Slapping-Robin, You-Dont-Say, 
Surprised-Pikachu, Batman-And-Superman, Dexter, Hello-Kassem, Mother-Of-God, Team-Rocket, Grumpy-Cat-Not-Amused, 
Engineering-Professor, Nice-Guy-Loki, Hillary-Clinton, Pope-Nicolas-Cage, Stoner-Dog, Minor-Mistake-Marvin, 
Fabulous-Frank-And-His-Snake, Oprah-You-Get-A, Smug-Bear, Surprised-Koala, Facepalm-Bear, Finn-The-Human, 
Felix-Baumgartner-Lulz, X-X-Everywhere, College-Freshman, Sexually-Oblivious-Girlfriend, Koala, Hawkward, 
Brian-Williams-Was-There, Meme-Dad-Creature, These-Arent-The-Droids-You-Were-Looking-For, Bad-Luck-Bear, 
Deadpool-Pick-Up-Lines, Subtle-Pickup-Liner, First-World-Problems, Crazy-Girlfriend-Praying-Mantis, Fk-Yeah, 
Butthurt-Dweller, Self-Loathing-Otter, Hal-Jordan, Member-Berries, Obama-Romney-Pointing, 
Perfection-Michael-Fassbender, Ancient-Aliens, Hypocritical-Islam-Terrorist, Apathetic-Xbox-Laser, Tom-Hardy-, 
Legal-Bill-Murray, Liam-Neeson-Taken-2, Rich-Guy-Dont-Care, Unsettled-Tom, Doug, Insanity-Wolf, Creeper-Dog, 
I-Am-Not-A-Gator-Im-A-X, Advice-Peeta, Overly-Manly-Man, Squidward, Captain-Picard-Facepalm, 
Keep-Calm-And-Carry-On-Aqua, Rick, Depression-Dog, Think, Tennis-Defeat, Multi-Doge, First-Day-On-The-Internet-Kid, 
Creepy-Condescending-Wonka, Blank-Blue-Background, Beyonce-Knowles-Superbowl-Face, Happy-Minaj-2, 
Feels-Bad-Frog---Feels-Bad-Man, Men-In-Black, Dafuq-Did-I-Just-Read, The-Critic, Keep-Calm-And-Carry-On-Purple, 
Jersey-Santa, TSA-Douche, Grus-Plan, Contradictory-Chris, Rick-and-Carl, Kim-Jong-Il-Y-U-No, 
Guy-Holding-Cardboard-Sign, College-Liberal, Paranoid-Parrot, Blank-Starter-Pack, Cute-Puppies, Nabilah-Jkt48, 
But-Thats-None-Of-My-Business-Neutral, Gasp-Rage-Face, Google-Chrome, Thats-Just-Something-X-Say, 
Face-You-Make-Robert-Downey-Jr, Officer-Cartman, Overly-Attached-Girlfriend, Pickup-Master, 
Musically-Oblivious-8th-Grader, Modern-Warfare-3, Pink-Escalade, Grumpy-Cat-Table, Evil-Kermit, Obama-Cowboy-Hat, 
Mr-T, Chester-The-Cat, Alien-Meeting-Suggestion, Homophobic-Seal, Serious-Xzibit, Snape, Picard-Wtf, Pelosi, 
Excited-Cat, Spiderman-Laugh, Portuguese, Rebecca-Black, Monkey-Business, Larfleeze, The-Rock-It-Doesnt-Matter, 
Intelligent-Dog, Britney-Spears, Dad-Joke-Dog, Arrogant-Rich-Man, Chemistry-Cat, Woman-Yelling-At-Cat, 
Cereal-Guys-Daddy, Little-Romney, Fear-And-Loathing-Cat, Art-Student-Owl, Putin, Talk-To-Spongebob, 
Mocking-Spongebob, Samuel-Jackson-Glance, Dat-Ass, Eye-Of-Sauron, Unicorn-MAN, Its-True-All-of-It-Han-Solo, 
Bill-OReilly, Internet-Guide, Harmless-Scout-Leader, Rick-Grimes, Baby-Cry, Predator, Romney, Jerkoff-Javert, 
Mega-Rage-Face, Actual-Advice-Mallard, Ron-Swanson, Burn-Kitty, Sudden-Disgust-Danny, Scrooge-McDuck-2, 
If-You-Know-What-I-Mean-Bean, Super-Cool-Ski-Instructor, Welcome-To-The-Internets, Annoying-Facebook-Girl, 
Bubba-And-Barack, Herm-Edwards, Romneys-Hindenberg, Impossibru-Guy-Original, Relaxed-Office-Guy, 
Determined-Guy-Rage-Face, Small-Face-Romney, Alyssa-Silent-Hill, Do-I-Care-Doe, Big-Bird-And-Snuffy, 
Aint-Nobody-Got-Time-For-That, Baron-Creater, Are-Your-Parents-Brother-And-Sister, Inception, Dont-You-Squidward, 
Back-In-My-Day, Secure-Parking, Challenge-Accepted-Rage-Face, Brian-Griffin, Murica, I-Know-That-Feel-Bro, 
Men-Laughing, Ghost-Nappa, Simsimi, Beyonce-Knowles-Superbowl, Internet-Explorer, Yao-Ming, Costanza, 
Felix-Baumgartner, Harper-WEF, Zuckerberg, Matanza, Anti-Joke-Chicken, Simba-Shadowy-Place, Beyonce-Superbowl-Yell, 
Pillow-Pet, Surprised-Coala, Fast-Furious-Johnny-Tran, Happy-Minaj, Michael-Phelps-Death-Stare, 
American-Chopper-Argument, Scumbag-Job-Market, Rick-and-Carl-3, Really-Evil-College-Teacher, WTF, 
Ridiculously-Photogenic-Judge, Okay-Truck, Good-Fellas-Hilarious"""

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


