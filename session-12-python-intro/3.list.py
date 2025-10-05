my_list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] #list of integers
print("my_list:", my_list)

print("element at index 1:", my_list[1]) #accessing element at index 1
my_list.append(11) #adding element 11 to the list
my_list[2]=22 #update value at index 3 to 22
print("my_list after changes:", my_list)

my_list.insert(0,12) #insert 12 at index 0
print("insert at 0:", my_list)

my_list.remove(12) #remove element 12 from the list
print("my_list after removing 12:", my_list)
my_list.pop() #remove last element from the list
my_list.pop(2) #remove element at index 2
print("my_list after popping index 2:", my_list)
print("length of my_list:", len(my_list)) #length of the list
