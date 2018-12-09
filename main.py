from clear_screen import clear_screen
from menu_options.multiple_choice import multiple_choice

clear_screen()

print("\nLANGUAGE LEARNING APP")
print("(type 'exit' to end program)\n")

print("\t1) Multiple Choice")
print("\t2) Fill-In the Blank")
print("\t3) Change Language")
print("\t4) Other")
selection = input("\nEnter 1 - 4 to choose: ")

try:
	if selection.lower() == 'exit':
		exit()

	elif int(selection) in range(1, 5):
		selection = int(selection)

		if selection == 1:
			multiple_choice()

		elif selection == 2:
			# fill_in_blank()
			clear_screen()
			print("Fill-in the blank mode is coming soon!")

		elif selection == 3:
			# change_language()
			clear_screen()
			print("Multiple language options are coming soon!")

		elif selection == 4:
			# other()
			clear_screen()
			print("Other features are coming soon!")

	else:
		print("Sorry, try again.")

except:
	print('Invalid input, exiting program.')