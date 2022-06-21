#!/usr/bin/env python3

from itertools import product
from math import ceil
from random import choice



def create_streak(moves, cartesan_product, length):
    def append_and_account(combo):
        streak.append(combo[1])
        counter[combo] += 1

    def check_for_duplication(to_append, min_count):
        for move in streak:
            if counter[(move, to_append)] == min_count:
                pass
            else:
                return (move, to_append)

    streak = []
    counter = {combo: 0 for combo in cartesan_product}
    c_prod_length = len(cartesan_product)

    first = choice(cartesan_product)
    streak.append(first[0])
    streak.append(first[1])
    counter[first] += 1

    while len(streak) != length:
        if (len(streak)) > c_prod_length:
            min_count = ceil(len(streak) / c_prod_length)
        else:
            min_count = 1
        to_append = choice(moves)
        combo = check_for_duplication(to_append, min_count)
        if combo:
            append_and_account(combo)
    return streak


def get_moves_from_file(school, schools_folder):
    # print(f"{schools_folder}/{school}/moves.txt")
    moves = []
    with open(f"{schools_folder}/{school}/moves.txt", "r") as file:
        for line in file.readlines():
            moves.append(line)
    return moves

def main(school, length, schools_folder, user_sounds=False):
    moves = get_moves_from_file(school, schools_folder)

    # * converting the output of product to list to avoid generator exhaustion
    cartesan_product = list(product(moves, moves))

    streak = create_streak(moves, cartesan_product, int(length))
    # print(streak)
    return streak


# TODO: length should be in minutes as well
# TODO: dynamic min count, so progress can be stored
# TODO: requirements.txt
# TODO: download voice file for each move
# TODO: drive integration
# TODO: ci/cd
# TODO: school combination and custom school creation
# TODO: totalcmd drive plugin???
# * requirements generation
# * pipreqs --savepath=requirements.in && pip-compile
