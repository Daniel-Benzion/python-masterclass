# Python3 has 5 built-in sequence types:
# > string
# > list
# > tuple
# > range
# > bytes and bytearray


# What is a sequence?
# An ordered set of items
# "Hello world"
# ["PC", "Speakers", "Keyboard", "Mouse"]

# Because a sequence is ordered, we can use indexing to access individual items in the sequence
# Almost everything you can do with a string can be done with the other sequence types
# However, not all sequence types can be multiplied or concatenated. For example, a range can't be concatenated.

string1 = "he's "
string2 = "probably "
string3 = "pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)

print("Hello " * 5)

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")


today = "friday"
print("day" in today)
print("fri" in today)
print("thur" in today)
