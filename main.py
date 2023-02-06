print("Hi there, type 'help' to see the menu.")
user_menu = 0
while user_menu < 1_0000000:
    user_first_interaction = input('>')
    user_menu += 1
    if user_first_interaction.upper() == "HELP":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit""")
        break
    else:
        print("I don't understand that...")
user_menu_2 = 0
while user_menu_2 < 1_0000000:
    user_response = input('>')
    user_menu_2 += 1
    if user_response.upper() == "START":
        print('Car started...Ready to go!')
    elif user_response.upper() == "STOP":
        print('Car stopped.')
    elif user_response.upper() == "QUIT":
        break
    else:
        print("I don't understand that")