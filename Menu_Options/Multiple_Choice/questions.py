from Menu_Options.Multiple_Choice.answers import ask_answer
from Menu_Options.Multiple_Choice.random_stuff import randomize_choices
from clear_screen import clear_screen


def ask_question(word, choices, answer, total):
    """Prints out question prompt"""

    print(f'Translate: {word}')

    choices = randomize_choices(choices)
    option_number = 1

    for choice in choices:
        print(f'\n {option_number}) {choice}')
        option_number += 1

    response = ask_answer(answer, choices, total)
    return response
