# max and min
print(max(2,3))
print(min([1,3,4,12,100]))

# sum
def even_check(num):
    if num % 2 == 0:
        print("Number was even")
    else:
        print("Odd number")

print(3 % 2)
print(100 % 10)

mylist = ['a', 'b', 'c']
index = 0
for letter in mylist:
    print('{} is at index: {}'.format(letter,index))
    index = index + 1

# enumerate
# keeping track of the index while iterating
for item in enumerate(mylist):
    print(item)

for index,item in enumerate(mylist):
    print("{} is at index {}".format(item,index))

# join
mylist = ['a', 'b', 'c', 'd']
# choose a string connector in between these elements then connect them together
print(''.join(mylist))

# PROBLEM 1
# Write a function that returns a boolean indicating if the word 'secret'
# is in a string
def secret_check(mystring):
    return 'secret' in mystring.lower()

print(secret_check("this is a Secret"))

# PROBLEM 2
# Create a code maker function that takes a string name and replace any vowels
# with the letter x
def code_maker(mystring):
    output = list(mystring)
    for index,letter in enumerate(mystring):
        if letter.lower() in 'aeiou':
            output[index] = 'x'
    output = ''.join(output)
    return output

print(code_maker('bellE vie'))
