def multiply(x, y):
    result = x * y
    return result


def is_palindrome(word):
    word = word.casefold()
    return word == word[::-1]

answer = multiply(10.5, 4)
print(answer)

print(is_palindrome("Tacocat"))