# Dictionaries
# Unordered mappings for storing objects
# {'key1':'value1','key2':'value2'}
# When to choose a list or a dict?
# Dict: values retrieved by the key username
# In a list you would have known the index location
# You can not sort a dict.
# Lists: objects retrieved by location
# They can be indexed and sliced
# You need to know the location of a value to retrieve it

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict)
print(my_dict['key1'])

salaries = {'John':20, 'Sally':30, 'Sammy':15}
salaries['Cindy'] = 100 # we do not need to call insert/append like in lists
print(salaries['Cindy'])

print(salaries['John'])

salaries['John'] = salaries['John'] + 40
print(salaries['John'])

# Nested dictionnary
people = {'John':{'salary':10, 'age':30}}
print(people['John']['age'])

d = {'k1':10,'k2':20,'k3':30}
print(d.keys())
print(d.values())
print(d.items())
