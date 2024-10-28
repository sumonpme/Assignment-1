#Removing elements from a tuple
Task_4=( 10,20,30, 10.5, 100)
temp_list = list(Task_4)
temp_list.remove(20)
new_tuple = tuple(temp_list)
print(new_tuple) 