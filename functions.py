def multiply(x, y):
    """
    Get the product of two numbers.

    Args:
        x: The first number to be multiplied.
        y: The second number, to be multiplied by x.
    Returns: 
        The result of multiplying x by y.
    """
    result = x * y
    return result


def is_palindrome(word):
    """
    Return True if a given string is a palindrome, False otherwise.
    
    A string is a palindrome if it is identical when its character order is reversed, ignoring capitalization.
    """
    word = word.casefold()
    return word == word[::-1]


def is_palindrome_sentence(sentence):
    result = "".join(char.casefold() for char in sentence if char.casefold() in "abcdefghijklmnopqrstuvwxyz")
    return result == result[::-1]

answer = multiply(10.5, 4)
print(answer)

print(is_palindrome("Tacocat"))
print(is_palindrome_sentence("A man a plan, a canal: panama."))

def sum_eo(n, t):
    result = 0
    if t == "e":
        if n % 2 == 0:
            n -= 2
            while n > 0:
                result += n
                n -= 2
            return result
        else:
            n -= 1
            while n > 0:
                result += n
                n -= 2
            return result
                
    elif t == "o":
        if n % 2 != 0:
            n -= 2
            while n > 0:
                result += n
                n -= 2
            return result
        else:
            n -= 1
            while n > 0:
                result += n
                n -= 2
            return result
            
    return -1

def sum_eo2(n, t):
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))