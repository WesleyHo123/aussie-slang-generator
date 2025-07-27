import random

"""
This is a program centered around Australian slang
"""

def learning_mode_instructions():
    """
    Display valid inputs to the user
    """
    print("Learning Mode Menu")
    print("Press 'Enter' to generate a random Australian slang")
    print("Press 'r' to return to the main menu")
    print("Press 'x' to exit the program entirely")
    print("")

def handle_input(exit_key,return_key,enter_key):
    """
    Accepting user input and formats the input to lower case letters.
    Handles errors when the user enters an unexpected input.
    Returns: user_input (str)
    """
    # prompts and accepts user input if it is 'Enter', 'r' or 'x'
    user_input = input("Please enter your input: ")

    # checks if the user enters the either exit key or the return key or blank space (for 'Enter')
    # keeps looping until the user enters valid user input
    while (user_input != exit_key) and (user_input != return_key) and (user_input != enter_key):
        user_input = input("Please a valid input: ")

    # converting input to lower case letters (X -> x, R -> r) to avoid conflicts
    user_input = user_input.lower()
    return user_input

def randomize_slang(slang_dictionary):
    """
    Main logic to randomize the slang
    Parameters: slang_dictionary (dict)
    Returns: random_slang (str), meaning (str)
    """
    # Obtains all key-value pairs like ('arvo', 'afternoon')
    slang_items = slang_dictionary.items()

    # Converting dictionary items into a list [('arvo', 'afternoon') ('brekkie', 'breakfast')...]
    slang_list = list(slang_items)

    # Using a list, the built in random.choice() function randomly selects an item from the list
    slang_and_meaning = random.choice(slang_list)
    # index 0 accessing the first item (the slang word) in the tuple
    random_slang = slang_and_meaning[0]
    # index 1 accessing the second item (the meaning) in the tuple
    meaning = slang_and_meaning[1]

    return random_slang, meaning

def learning_mode(aussie_slang,exit_key,return_key,enter_key):
    """
    Program 1: Learning mode
    Parameters: aussie_slang (dict), exit_key (str), return_key (str), enter_key (str)
    Returns: user_input (str)
    """

    #Display instructions and accepts valid user input
    learning_mode_instructions()
    user_input = handle_input(exit_key,return_key,enter_key)

    #check if the user enters 'x' or 'r'
    while (user_input != exit_key) and (user_input != return_key):

        #storing the slang and meaning into variables obtained from the aussie_slang dictionary
        random_slang, meaning = randomize_slang(aussie_slang)

        print("Input received!")
        print(f"Slang: {random_slang}")
        print(f"Meaning: {meaning}")
        print("")
        #prompt users again to see if they want to continue, return to main menu or exit the program
        learning_mode_instructions()
        user_input = handle_input(exit_key,return_key,enter_key)
    return user_input

def quiz_mode_instructions():
    """
    Display valid inputs to the user
    """
    print("Quiz Mode Menu")
    print("Press 'Enter' to generate a random Australian slang and try you best to answer correctly.")
    print("Press 'r' to return to the main menu")
    print("Press 'x' to exit the program entirely")
    print("")


def quiz_mode(aussie_slang, exit_key, return_key, enter_key):
    """
     Program 2: Quiz mode
     Parameters: aussie_slang (dict), exit_key (str), return_key (str), enter_key (str)
     Returns: user_input (str)
     """
    # Display instructions and accepts valid user input
    quiz_mode_instructions()
    user_input = handle_input(exit_key, return_key, enter_key)

    while (user_input != exit_key) and (user_input != return_key):
        random_slang, meaning = randomize_slang(aussie_slang)

        # for debugging only: To show current slang and the input required for 'meaning'
        print(f"Slang: {random_slang}")
        print(f"Meaning: {meaning}")

        #Prompt for user's answer for the slang
        user_answer = input(f"The slang is: {random_slang}. Please enter the meaning: ")
        #convert the user's answer and the meaning obtained from the dictionary to be all lowercase
        user_answer_lowercase = user_answer.lower()
        meaning_lowercase = meaning.lower()
        #check if the user's answer matches the meaning
        if user_answer_lowercase == meaning_lowercase: #if the answer is correct
            print(f" You are correct! The meaning for '{random_slang}' is: {meaning}")
        elif user_answer_lowercase != meaning_lowercase: #if the answer is incorrect
            print(f" Sorry! Your are incorrect.The meaning for '{random_slang}' is: {meaning}.")

        print("")
        # prompt users again to see if they want to continue, return to main menu or exit the program
        quiz_mode_instructions()
        user_input = handle_input(exit_key, return_key, enter_key)
    return user_input

def introduction_msg():
    """
    What the user sees when the program first runs
    """
    print("MAIN MENU")
    print("Enter '1' to enter 'Learning mode' to generate a random Australian slang and learn its meaning")
    print("Enter '2' to enter 'Quiz mode' and test your knowledge on Australian slangs")
    print("Enter 'x' to exit the program")
    program_selection = input("Please select an option: ")
    #check if the str is '1' or '2' or 'x', if it is not, prompts for a valid input
    while(program_selection != "1" and program_selection != "2" and program_selection != "x"):
        program_selection = input("Please select a valid option '1' or '2' or 'x': ")
    print("")
    return program_selection

def handle_menu_flow(user_input,exit_key,return_key):
    """
    Handles user entering 'x' to ecit the program or 'r' to return to the main menu
    Return: 'exit'(str), 'continue', or 'return'
    """
    if user_input == exit_key:
        return False  # Acts as like a 'break'/exit
    elif user_input == return_key:
        return True  # Acts like a 'pass'
    else:
        return True # For users entering '1' or '2'

def exit_msg():
    print("Thank you for using this program!")
    print("Now exiting...")

def main():
    """
    creates a dictionary that stores the slang and meanings
    ###IMPORTANT###
    Make sure there are no spaces after the 'meaning'.
    For example, "Afternoon" is correct
    "Afternoon " is incorrect and causes errors for intended use
    ######

    initiates dedicated keys for menu selection
    """

    aussie_slang = {
        "Arvo": "Afternoon",
        "Avo": "Avocado",
        "Brolly": "Umbrella",
        "Brekky": "Breakfast",
        "Coldie": "Beer",
        "Coppers": "Policemen",
    }
    # define keys for exiting the program or returning to the main menu
    exit_key = 'x'
    return_key = 'r'
    enter_key = ""

    while True:
        user_input = introduction_msg()

        if not handle_menu_flow(user_input, exit_key, return_key):
            break
        elif user_input == '1':
            user_input = learning_mode(aussie_slang,exit_key,return_key,enter_key)
            #for debugging
            #print(f"DEBUG: learning_mode returned: '{user_input}'")
            if not handle_menu_flow(user_input, exit_key, return_key):
                break
        elif user_input == '2':
            user_input = quiz_mode(aussie_slang, exit_key, return_key, enter_key)
            # for debugging
            #print(f"DEBUG: quiz_mode returned: '{user_input}'")
            if not handle_menu_flow(user_input, exit_key, return_key):
                break

    exit_msg()


if __name__ == "__main__":
    main()
