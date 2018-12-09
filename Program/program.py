import os
import csv
import random

MENU = ''
TOTAL_ANSWERED = 0
KNOWN_WORDS_LOCATION = 'known_words.dictionary'
RUNNING = True
PROGRAMS = ['Multiple Choice', 'Exit']

def clear_screen():
    """Clears screen"""
    os.system('cls' if os.name == 'nt' else 'clear')
    return


def csv_to_list(csv_file):
    with open(csv_file, 'rt') as file:
        reader = csv.reader(file)
        return list(reader)


def ask_answer(answer, choices):
    """Prints answer promt and returns user input as a boolean"""
    response = input('\nChoose 1 - 4 and press Enter: > ')

    if response.lower() == 'exit':
        end_program()

    validity = check_validity(response, choices, answer)

    return validity


def check_validity(response, choices, answer):
    """Check if response is valid"""
    clear_screen()

    index = int(response) - 1

    if index in range(4):
        response = choices[index]
        correctness = check_correctness(answer, response)
        
        return correctness
    else:
        print('Answer not valid. Enter 1, 2, 3 or 4.\n')
    
        return False


def check_correctness(answer, response):
    """Check if answer is correct or not"""
    global TOTAL_ANSWERED

    if response == answer:
        TOTAL_ANSWERED += 1

        print('Nice work! You got it!\n')

        return True
    else:
        print('Sorry try again.\n')

        return False

def end_program():
    global MENU
    clear_screen()

    print(f'You got {TOTAL_ANSWERED} questions right!')
    show_menu(MENU)


def randomize_choices(choices):
    """Returns a random list from an orderd list"""
    rand_set = set()
    choices = list(choices)

    while len(rand_set) != len(choices):
        target = random.randrange(len(choices))
        
        rand_set.add(choices[target])

    return list(rand_set)


def rand_row(word_list, question=True, used_words=set()):
    """Returns a random row for both a question with
       answer and random spanish words for multiple choices
       depending on if question is True"""
    done = False
    
    while not done:
        random_row = random.randrange(100)
        row = word_list[random_row]
        word = row[1]
        answer = row[4]

        if question:
            if word not in used_words:
                used_words.add(word)

                done = True
                
                return word, answer
            else:
                continue

        else:
            done = True

            return answer


def ask_question(word, choices, answer):
    """Prints out question prompt"""

    print(f'Translate: {word}')
    
    choices = randomize_choices(choices)
    option = 1

    for choice in choices:
        print(f'\n {option}) {choice}')
        option += 1

    response = ask_answer(answer, choices)
    return response


def read_from_file(file_path):
	read_file = open(file_path, 'r').read()
	dictionary = eval(read_file)

	return dictionary


def save_to_file(dictionary, file_path):
	write_file = open(file_path, 'w')
	
	write_file.write(str(dictionary))
	write_file.close


def find_difficulty(word):
    """A prompt asking the difficulty of each question"""
    difficulty = 0

    while difficulty not in range(1, 6):
        try:
            difficulty = input('Rate difficulty from 1(EASY) to 5(HARD): ')
            difficulty = int(difficulty)

            if difficulty in range(1, 6):
                clear_screen()

                known_words = read_from_file(KNOWN_WORDS_LOCATION)
                
                known_words[difficulty].append(word)

                save_to_file(known_words, KNOWN_WORDS_LOCATION)

        except:
            difficulty = 0


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


def run_program(selection):
    """The following is like a switch_case statment, depending on the
    selection from the user in option_selecetion it will run one of the
    following as a function"""
    switch_case = {
    1: multiple_choice,
    2: exit
    }
    func = switch_case.get(selection)
    func()


def option_selection(list_of_programs=PROGRAMS):
    """Collects selection from user input and sanitize their input"""
    selection = input('\nChoose an option from the list: ')
    try:
        if selection.lower() == 'exit':
            exit()
        selection = int(selection)
        # The following will cause a index error if selection out of
        # range in list_of_programs
        list_of_programs[selection-1]
        if selection == 0:
            raise IndexError
        run_program(selection)

    except ValueError:
        clear_screen()
        print("PLEASE USE NUMBERS TO MAKE SELECTION.")
        show_menu(MENU)

    except IndexError:
        clear_screen()
        print('THAT OPTION IS NOT IN THE LIST.')
        show_menu(MENU)



def show_menu(menu):
    """Shows the created menu from make_menu, to reuse send MENU as a
    paramater"""
    print(menu)
    option_selection()


def make_menu(list_of_programs=PROGRAMS):
    """This will create the menu that we can reuse and show with the 
    function show_menu over and over again. Makes it once, but shows it 
    several times."""
    global MENU
    clear_screen()
    menu_str = "\nLANGUAGE LEARNING APP\n(type 'exit' to end a program)\n"
    option_number = 1
    for item in list_of_programs:
        option = f'\n{option_number}.) {item}'
        menu_str += option
        option_number += 1
    MENU = menu_str
    show_menu(MENU)

	# if selection.lower() == 'exit':
	# 	exit()

	# elif int(selection) in range(1, 5):
	# 	selection = int(selection)

	# 	if selection == 1:
	# 		multiple_choice()

	# 	elif selection == 2:
	# 		# fill_in_blank()
	# 		clear_screen()
	# 		print("Fill-in the blank mode is coming soon!")

	# 	elif selection == 3:
	# 		# change_language()
	# 		clear_screen()
	# 		print("Multiple language options are coming soon!")
	# 	elif selection == 4:
	# 		# other()s
	# 		clear_screen()
	# 		print("Other features are coming soon!")

	# else:
	# 	print("Sorry, try again.")
