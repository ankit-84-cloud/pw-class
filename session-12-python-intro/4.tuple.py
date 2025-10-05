my_tuple = (1, 2, 3, 4, 5, 6) #tuple of integers
print(my_tuple)
print("element at index 2:", my_tuple[2]) #accessing element at index 2
print ("element at index -2:", my_tuple[-2]) #accessing second last element using negative index
print("element at index -3:", my_tuple[-3]) #accessing third last element using negative index

#my_tuple[1]=67
#error to assign valu to tuple

print("count of 2 in tuple: ",(1,2,3,2,3,2,1).count(2)) #counting occurrences of 2 in the tuple
print("index of 3 in tuple: ",(1,2,3,2,3,2,1).index(3)) #finding index of first occurrence of 3 in the tuple