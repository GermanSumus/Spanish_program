from qna.answers import ask_answer
from random_stuff import randomize_choices
from clear_screen import clear_screen

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