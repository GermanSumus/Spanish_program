from clear_screen import clear_screen
from Menu_Options.Multiple_Choice.questions import ask_question
from Menu_Options.Multiple_Choice.random_stuff import rand_row
from time import time
import csv
import json

KNOWN_WORDS_LOCATION = 'dataFiles/known_words.txt'

def difficulty(word, difficulty):
    try:
        with open(KNOWN_WORDS_LOCATION, 'r') as file:
            known_words = json.loads(file.read())
    except FileNotFoundError:
        known_words = dict()
    if str(difficulty) in known_words:
        known_words[str(difficulty)].append(word)
    else:
        known_words.update({difficulty:[word]})
    with open('dataFiles/known_words.txt', 'w+') as file:
        json.dump(known_words, file)
def csv_to_list(csv_file):
    with open(csv_file, 'rt') as file:
        reader = csv.reader(file)
        return list(reader)

def multiple_choice():
    clear_screen()

    while True:
        csv_file = 'dataFiles/100_words.csv'

        word_list = csv_to_list(csv_file)

        choices = set()

        word, answer = rand_row(word_list)
        choices.add(answer)

        while len(choices) <= 3:
            choices.add(rand_row(word_list, question=False))

        correct = False
        _ = time()
        while not correct:
            correct = ask_question(word, choices, answer)
        __ = time()
        seconds = int(__-_)
        difficulty(word, seconds)
