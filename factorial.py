def factorial(num: int) -> int:
    """
    Return n! (0! is 1).
 
    Valid for `n` in the range 0 to 998 (inclusive).
    Larger values of `n` will cause a RecursionError.
    """
    if num <= 1: return 1
    
    return num * factorial(num - 1)