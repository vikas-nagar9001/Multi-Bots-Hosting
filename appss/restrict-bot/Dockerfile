FROM python:3.10.8-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD gunicorn app:app & python3 bot.py



# Don't Remove Credit Tg - @Mod_Mick
# Ask Doubt on telegram @Mod_Mick