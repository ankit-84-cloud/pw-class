my_set = {1, 2, 3, 2, 4, 2, 5, 6} #set of integers #unordered set
print("my_set:", my_set) #you can see duplicates are removed
my_set.add(7) #adding element 7 to the set
print("my_set after adding 7:", my_set) #adding duplicate element will have no effect
my_set.remove(3) #removing element 3 from the set
print("my_set after removing 3:", my_set)

my_set.pop()   #removing any random element from the set
print("my_set after popping an element:", my_set)

my_set.discard(35) #if element present delete if not then leave it, not throwing error