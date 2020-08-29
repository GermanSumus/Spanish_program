from clear_screen import clear_screen
from time import sleep


def ask_answer(answer, choices, total):
    """Prints answer promt and returns user input as a boolean"""
    user_response = input('Choose 1 - 4 and press Enter: > ')

    if user_response.lower() == 'exit':
        end_program(total)
    try:
        user_response = int(user_response)
    except ValueError:
        print('Numbers Please.')
        sleep(1)
        return False
    validity = check_validity(user_response, choices, answer)

    return validity

def check_validity(user_response, choices, answer):
    """Check if user_response is valid"""

    index = int(user_response) - 1

    if index in range(4):
        user_response = choices[index]
        correctness = check_correctness(answer, user_response)

        return correctness
    else:
        print('Answer not valid. Enter 1, 2, 3 or 4.')
        sleep(1)
        return False

def check_correctness(answer, user_response):
    """Check if answer is correct or not"""

    if user_response == answer:
        print('Nice work! You got it!')
        sleep(1)
        return True
    else:
        print('Sorry try again.')
        sleep(1)
        return False

def end_program(total):
    clear_screen()

    print(f'You got {total} questions right!')

    exit()
