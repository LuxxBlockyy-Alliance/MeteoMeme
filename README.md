# MeteoMeme 🤖🌤️

Willkommen zu **MeteoMeme** - dem lustigen Discord-Bot, der das aktuelle Wetter in ein humorvolles Meme verwandelt! 🌞😂

## Übersicht

Für den Mini Hackathon von Kevin Chromik haben wir uns entschieden, etwas Außergewöhnliches zu entwickeln. Statt einer traditionellen Wetter-App haben wir einen Discord-Bot programmiert, der mithilfe der OpenMeteo API und GPT-4 Turbo Wetterinformationen sammelt und diese in Form eines Memes darstellt. Dies wird durch den apimeme.com Endpoint ermöglicht. So wird das Wetter auf eine humorvolle Weise präsentiert!

## Funktionen

- **Wetter-Meme Generierung**: Nutze den Slash Command `/wetter` gefolgt von einer Stadt, um ein Meme basierend auf dem aktuellen Wetter dieser Stadt zu erhalten.
- **Einfache Integration**: Der Bot kann problemlos zu deinem Discord-Server hinzugefügt werden.

## Beispiel

![MeteoMeme Beispiel 1](https://api.memegen.link/images/sad-boehner/Wenn_das_Gewitter_deine_Grillparty_ruiniert/Bielefeld,_23_Grad.png)
![MeteoMeme Beispiel 1](https://media.discordapp.net/attachments/1262423635746881647/1262445308109918278/image.png?ex=66969f50&is=66954dd0&hm=4aaf3a5903ed77c1237c2e8f800fd15e4fa092fa0a68bc5b841f193ebbff3600&=&format=webp&quality=lossless)

## Installation und Einrichtung

### Voraussetzungen

- Python 3.8+
- Ein Discord Bot Token
- OpenAI API Key

### Schritte

1. **Repository klonen**
   ```sh
   git clone https://github.com/LuxxBlockyy-Alliance/MeteoMeme.git
   cd MeteoMeme
   ```

2. **Virtuelle Umgebung erstellen und aktivieren**
   ```sh
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   .\venv\Scripts\activate    # Windows
   ```

3. **Abhängigkeiten installieren**
   ```sh
   pip install -r requirements.txt
   ```

4. **Konfigurationsdatei anpassen**
   Konfiguriere die Datei namens `config.ini` im Hauptverzeichnis mit folgendem Inhalt:
   ```ini
   [KEYS]
   openai_key = DEIN_OPENAI_API_KEY
   discord_bot_token = DEIN_DISCORD_TOKEN
   ```

5. **Bot starten**
   ```sh
   python app.py
   ```

## Bot zu deinem Discord-Server hinzufügen

Klicke auf den folgenden Link, um den Bot zu deinem Server hinzuzufügen: [MeteoMeme zu deinem Server hinzufügen](https://discord.com/oauth2/authorize?client_id=1262437648304443412)

## Testen

Tritt unserem Test-Discord-Server bei, um den Bot in Aktion zu sehen und ihn auszuprobieren: [MeteoMeme Test Server](https://discord.gg/RXxgxveERY)

## Beitragende

- **Janosch | blockyy**
- **Luxx**

---

Wir hoffen, dass dir unser Bot genauso viel Spaß macht wie uns bei der Entwicklung! Bei Fragen oder Feedback, tritt unserem [Discord Server](https://discord.gg/RXxgxveERY) bei.

Viel Spaß beim Memes generieren! 🎉
