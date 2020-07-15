from clear_screen import clear_screen
from Menu_Options.Multiple_Choice import multiple_choice
from time import sleep


def main_menu():
    clear_screen()
    print("LANGUAGE LEARNING APP")
    print("(type 'exit' to end program)\n")
    print("\t1) Multiple Choice")
    print("\t2) Family")
    print("\t3) Change Language")
    print("\t4) Other")
    selection = input("\nEnter 1 - 4 to choose: ")
    try:
        if selection.lower() == 'exit':
            print("Exiting Program")
            exit()
        else:
            selection = int(selection)
    except ValueError:
        # No number entered in, unable to find number in selection
        print('That\'s not a valid entry, please try again.')
        sleep(1)
        main_menu()

    if selection == 1:
        multiple_choice.multiple_choice('dataFiles/100_words.csv')
    elif selection == 2:
        # fill_in_blank()
        clear_screen()
        multiple_choice.multiple_choice('dataFiles/family.csv')
        # print("Fill-in the blank mode is coming soon!")
        # sleep(1)
        # main_menu()
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
        main_menu
main_menu()
