menu = [
    ['egg', 'bacon'],
    ['egg', 'sausage', 'bacon'],
    ['egg', 'spam'],
    ['egg', 'bacon', 'spam'],
    ['egg', 'bacon', 'sausage', 'spam'],
    ['spam', 'bacon', 'sausage', 'spam'],
    ['spam', 'sausage', 'spam', 'bacon', 'spam', 'tomato', 'spam'],
    ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam']
]

for meal in menu:
    if "spam" in meal:
        max = len(meal) - 1
        for index, item in enumerate(reversed(meal)):
            if item == "spam":
                del meal[max - index]

    print(meal)

for meal in menu:
    items = ", ".join(item for item in meal if item != "spam")
    print("[", items, "]", sep="")