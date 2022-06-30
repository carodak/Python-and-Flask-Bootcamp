# TUPLES
t = (1,2,3,'a')
my_list = [1,2,3,'a']
my_list[0] = 'b'
print(my_list)

#t[0] = 'b' Error we can't do the reassignement
# We will use tuples for things that won't change
# Calendars..
print(t)

# SETS
x = set()
print(x)
x.add(1)
x.add(2)
x.add(3)
x.add(3) #sets = unique elements
x.add(3)
print(x)

my_list = [1,2,1212,22,2,2,2,2,1,5,6,1,1,1,1,1,3,4,4]
print(set(my_list))

# BOOLLEANS
a = True
b = False
# SPECIAL KEYWORD
c = None

print(a)
print(1 > 2)
