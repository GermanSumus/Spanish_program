from clear_screen import clear_screen
from Menu_Options.Multiple_Choice import multiple_choice
from time import sleep


def validate(func):
# Returns a valid integer response from user and calls func until then
    user_response = input("\nEnter 1 - 4 to choose >  ")
    if user_response.lower() == 'exit':
        print("Exiting Program")
        exit()
    try:
        return int(user_response)
    except ValueError:
        # No number entered in, unable to find number in selection
        print('Numbers Please.')
        sleep(1)
        func()

def main_menu():
    """
Creates our main menu with possible options of spanish learning activites or
list to learn. Function calls its self over and over until valid selection is
made or user types in 'exit'.
    """
    clear_screen()
    print("LANGUAGE LEARNING APP")
    print("(type 'exit' to end program)\n")
    print("\t1) Multiple Choice")
    print("\t2) Family")
    print("\t3) Change Language")
    print("\t4) Other")

    selection = validate(main_menu)

# Selection Choices
    if selection == 1:
        multiple_choice.multiple_choice('dataFiles/100_words.csv')
    elif selection == 2:
        clear_screen()
        multiple_choice.multiple_choice('dataFiles/family.csv')
    elif selection == 3:
        # change_language()
        clear_screen()
        print("Multiple language options are coming soon!")
        sleep(1)
        main_menu()
    elif selection == 4:
        # other()
        clear_screen()
        print("Other features are coming soon!")
        sleep(1)
        main_menu()
    else:
        print('That\'s not a valid entry, please try again.')
        sleep(1)
        main_menu()

main_menu()
