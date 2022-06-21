#!/usr/bin/env python3

from browser import document, html
from hitstreak import main as hitstreak

SCHOOLS_FOLDER = './schools'

def get_streak(event):
    global SCHOOL
    SCHOOL = document['school'].value.strip().rstrip()
    length = document['length'].value.strip().rstrip()
    global streak
    streak = hitstreak(SCHOOL, length, SCHOOLS_FOLDER)
    print(streak)

    first_move = streak.pop(0).rstrip()
    document['current'].textContent = f"{first_move}"
    move_count = 1
    document['counter'].textContent = 1
    document['player'].attrs['src'] = f"{SCHOOLS_FOLDER}/{SCHOOL}/{first_move}.mp3"


document["get_streak"].bind("click", get_streak)


def nexte(event):
    current_move = streak.pop(0).rstrip()
    move_count = document['counter'].textContent
    document['counter'].textContent = int(move_count) + 1
    document['current'].textContent = f"{current_move}"
    document['player'].attrs['src'] = f"{SCHOOLS_FOLDER}/{SCHOOL}/{current_move}.mp3"
    document['player'].play()

document['player'].bind("ended", nexte)