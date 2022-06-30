my_list = [1,2,3,"une fleur",2.]
print(my_list)
print(my_list[1:4])

my_list.append('z') # do an inplace
my_list.insert(0,'sauvage')
popped_item = my_list.pop(1)
print(my_list)
print(popped_item)

# NESTED LIST
my_list_1 = [0,1,2]
my_list_2 = [3,4,5]
my_list_3 = [6,7,8]

mega_list = [my_list_1,my_list_2,my_list_3]
print(mega_list)
print(mega_list[2][1]) #stack indexing with a nested list 
