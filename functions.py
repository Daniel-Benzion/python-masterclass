def multiply(x, y):
    result = x * y
    return result


def is_palindrome(word):
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