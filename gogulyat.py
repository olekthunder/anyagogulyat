import requests
import os

from datetime import datetime, timedelta
from creds import GIPHY_HASH, ANYA
import random
from client import client
from utils import get_week_day

GIPHY_PLEASE_URL = (
    f"https://api.giphy.com/v1/gifs/random?tag=sad&api_key={GIPHY_HASH}&limit=5"
)

GIF_TMP_FILE = 'my_tmp_gif.gif'

QUESTIONS = [
    "Аня, го гулять?",
    f"Сегодня уже {get_week_day(datetime.today()).lower()}, "
    "а мы не гуляем. Может, пора?",
    "Хочу сказать, что мы гуляли очень давно, поэтому пора. Буш?",
    "Аннмихална, я пишу не просто так, а с деловым предложением. Го гулять?",
    "Ага, попалась! Таки прочитала сообщение. Го гулять?",
    "Найди картинку грустного котика в интернете. Посмотри на него."
    "Он грустит, потому что мы не гуляем. Давай не расстраивать котика?",
    f"Привет. Завтра "
    f"{get_week_day(datetime.today() + timedelta(days=1)).lower()}, а "
    "это значит, что нам пора гулять",
]


def get_random_message():
    return random.choice(QUESTIONS)


def get_random_please_giph():
    giphy_url = requests.get(
        GIPHY_PLEASE_URL
    ).json()["data"]["image_original_url"]
    with open(GIF_TMP_FILE, 'wb') as giph_file:
        giph_file.write(requests.get(giphy_url).content)


def main():
    with client:
        client.send_message(ANYA, get_random_message())
        get_random_please_giph()
        client.send_file(ANYA, GIF_TMP_FILE)
        os.remove(GIF_TMP_FILE)


if __name__ == "__main__":
    main()
