from csv_to_list import csv_to_list
from clear_screen import clear_screen
from qna.questions import ask_question
from random_stuff import rand_row
from how_difficult import find_difficulty

def multiple_choice():
	clear_screen()

	while True:
		csv_file = '100_words.csv'
		word_list = csv_to_list(csv_file)

		choices = set()

		word, answer = rand_row(word_list)
		choices.add(answer)

		while len(choices) <= 3:
			choices.add(rand_row(word_list, question=False))

		correct = False

		while not correct:
			correct = ask_question(word, choices, answer)

		find_difficulty(word)