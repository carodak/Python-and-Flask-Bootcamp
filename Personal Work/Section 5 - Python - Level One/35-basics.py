print("Hello! Altough I use Python often, I wanted to start for scratch again and see if I do not miss any basis")

add1 = 15 + 2*3 + 7
print("First addition result: ", add1)

print(len("hel lo"))

my_string = "hellomylove"

# INDEXING
print(my_string[3])

# SLICING - [start:stop:step]
print(my_string[0:7])
print(my_string[0:7:3])
print(my_string[:7:3])
print(my_string[::-1])

# IMMUABLE STRING
#my_string[1] = s -> error

# USEFUL METHODS
my_second_string = "Hello " + "dear"
print(my_second_string)
print(my_second_string.upper())
print(my_second_string.lower())
print(my_second_string.split())
print(my_second_string.split('d'))

# FORMATING
username = "Cumin"
color = 'black and white'
print("{} color is {}".format(username, color))
# PYTHON 3.6 AND ABOVE
# f string literals
#print(f"The {username} chose {color}")
