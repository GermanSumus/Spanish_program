from clear_screen import clear_screen
from time import sleep

total_answered = 0

def ask_answer(answer, choices):
    """Prints answer promt and returns user input as a boolean"""
    user_response = input('\nChoose 1 - 4 and press Enter: > ')

    if user_response.lower() == 'exit':
        end_program()
    try:
        user_response = int(user_response)
    except ValueError:
        clear_screen()
        print('Answer not valid. Enter 1, 2, 3 or 4.\n')
        return False
    validity = check_validity(user_response, choices, answer)

    return validity


def check_validity(user_response, choices, answer):
    """Check if user_response is valid"""
    clear_screen()

    index = int(user_response) - 1

    if index in range(4):
        user_response = choices[index]
        correctness = check_correctness(answer, user_response)

        return correctness
    else:
        print('Answer not valid. Enter 1, 2, 3 or 4.\n')

        return False


def check_correctness(answer, user_response):
    """Check if answer is correct or not"""
    global total_answered

    if user_response == answer:
        total_answered += 1

        print('Nice work! You got it!\n')

        return True
    else:
        print('Sorry try again.\n')

        return False

def end_program():
    clear_screen()

    print(f'You got {total_answered} questions right!')

    exit()
