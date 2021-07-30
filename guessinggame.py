import random

def get_integer():
    """
    Gets an integer from Standard Input (stdin).
    
    The function will continue looping and prompting the user until a valid `int` is entered.

    Returns: The integer that the user enters.
    """
    while True:
        temp = input()
        if temp.isnumeric():
            return int(temp)
        else:
            print("That is not a valid input. Please enter an integer between 1 and 10.")


answer = random.randint(1, 10)
print("Guess a number between 1 and 10: ")

while True:
    guess = get_integer()

    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print("You got it!")
        break


print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)


print()
print("*" * 80)
help(input)
print("*" * 80)
help(get_integer)
print("*" * 80)

# tree1 = 'Oak'
# tree2 = 'Ash'

# if tree1 == tree2:
#     print("The trees are the same")
# else:
#     print("The trees are different")

# x = 5
# y = 7

# if x > y:
#     print("x is greater than y")
# elif x < y:
#     print("x is smaller than y")
# else:
#     print("x equals y")

# print()

# print("x equals y") if x == y else print("x is greater than y") if x > y else print("x is smaller than y")