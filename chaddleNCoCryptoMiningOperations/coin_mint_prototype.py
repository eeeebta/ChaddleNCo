from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import random

import re
import hashlib


def break_lines_16(string_inp):
    return '\n'.join(re.findall('.{1,16}', string_inp))


def generate_coin(coin_hash, phrase):
    with open("num.txt", "r") as f:
        num = int(f.readline())

    img = Image.open("chaddlecoin_temp.jpg")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(<font-file>, <font-size>)

    # Font size for number of minted coin
    font_num = ImageFont.truetype("VT323-Regular.ttf", 128)

    # Hex font size on pig
    font_hex = ImageFont.truetype("VT323-Regular.ttf", 32)

    # Font size for pig forehead
    font_mine = ImageFont.truetype("VT323-Regular.ttf", 16)
    draw.text((320, 110), f"{num}", (255, 255, 255), font=font_num)
    draw.text((964, 100), f"{break_lines_16(coin_hash)}", (255, 255, 255), font=font_hex)
    draw.text((1225, 50), f"Mined: {phrase}", (0, 0, 0), font=font_mine)

    img.save(f"chaddlecoin_mint_{num}.jpg")
    num += 1
    with open("num.txt", "w+") as f:
        f.write(str(num))


def generate_phrase():
    with open("nouns.txt", "r") as f:
        nouns = f.readlines()

    word = random.choice(nouns).capitalize()
    # while len(word) < 9:
    #     word = random.choice(nouns).capitalize()

    return f"Chads{word}"

