def func(p1, p2, *args, k, **kwargs):
    print("positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))


func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)

# positional-or-keyword:...1, 2
# var-positional (*args):..(3, 4, 5)
# keyword:.................6
# var-keyword:.............{'key1': 7, 'key2': 8}

def sum_numbers(*args: float) -> float:
    """ calculates the sum of all the numbers passed as arguments """
    return sum(args)