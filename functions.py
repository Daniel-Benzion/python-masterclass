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