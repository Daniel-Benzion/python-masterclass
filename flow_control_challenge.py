while True:
    user_input = input("""Choose an option: 
    1:\tLearn Python
    2:\tLearn Java
    3:\tGo swimming
    4:\tHave dinner
    5:\tGo to bed
    0:\tExit
    """)
    is_valid = user_input == "1" or user_input == "2" or user_input == "3" or user_input == "4" or user_input == "5" or user_input == "0"
    if is_valid:
        if int(user_input) == 0:
            print("Byeeeeee")
            break
        elif 0 < int(user_input) < 6:
            print("Valid.")
            print("Press enter to continue")
            input()
    else:
        print("Invalid response. Enter a number.")
        print("Press enter to continue")
        input()