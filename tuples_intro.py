t = "a", "b", "c"
print(t)

s = ("a", "b", "c")
print(s)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imelda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica = list(metallica)
metallica[0] = "Master of Puppets"
metallica[2] = 1986

metallica = tuple(metallica)

print(metallica)