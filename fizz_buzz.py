def fizz_buzz(num: int) -> str:
    """
    FizzBuzz number checker.
    
    :param num: The number to check
    :return:
        "fizz" if `num` is divisible by 3.

        "buzz" if `num` is divisible by 5.

        "fizz buzz" if `num` is divisible by both 3 and 5.

        Otherwise, return `str(num)`
    """
    if num % 15 == 0:
        return "fizz buzz"
    elif num % 3 == 0:
        return "fizz"
    elif num % 5 == 0:
        return "buzz"
        
    return str(num)

# print(", ".join(fizz_buzz(i) for i in range(1, 101)))

def play_fizz_buzz():
    """
    Play FizzBuzz with the computer.
    Gameplay ends when the player either makes a mistake or gets to 100.
    """

    print("Let's play FizzBuzz! I'll go first.")
    current = 1
    while(current <= 100):
        print(fizz_buzz(current))
        current += 1
        if (current < 100):
            user_input = input()
            if fizz_buzz(current) != user_input:
                break
            current += 1
    else:
        print("You win!")


play_fizz_buzz()
