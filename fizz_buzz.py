def fizz_buzz(num: int) -> str:
    """
    Play FizzBuzz.
    
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

print(", ".join(fizz_buzz(i) for i in range(1, 101)))