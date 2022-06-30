seq = [1,2,3,4,5]

for num in seq:
    print(num)

mystring = 'hello'

for char in mystring:
    print(char)

salaries = {'John' : 20, 'Sally' : 30, 'Lisa' : 30}
for employee in salaries:
    salary = salaries[employee]
    print(employee)
    print("has a salary of:")
    print(salary)

mypairs = [('a',1),('b',2),('c',3)]

for item in mypairs:
    print(item)
# TUPLE UNPACKING!!
for (letter,num) in mypairs:  #unpacking the tuples (tuples are very common in python so you can do it like this)
    print(letter)
    print(num)

i = 1
while i < 5:
    print("is is currently: {}".format(i))
    i = i + 1

# USEFUL OPERATORS
for x in range(0,5):
    print(x)

result = list(range(0,11,2))
print(result)

print('z' in 'sdsdnjlsdsndsjdslkdpsdip') #in operator = check if an element is inside another one
print(1 in [1,2,3])
