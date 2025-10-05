my_dict={
    "name":"John",
    "age":30,
    "city":"New York",
    "expertise":["Devops" ,"Cloud" ,"Python" ,"AWS" ,"Docker" ,"Kubernetes"]
}
#print( my_dict)
print("name: ",my_dict["name"]) #accessing value using key
my_dict['manager']="test manager" #adding new key-value pair
# print( my_dict)

#iterate one by onec
for key in my_dict:
    if(isinstance(my_dict[key], list)):
        print(f"{key}:")
        for item in my_dict[key]:
            print("  - ", item)
    else:
        print(key," : ",my_dict[key])

    my_dict.pop("age") #removing based on key if key not available it will throw an error
    print(my_dict)

my_dict.popitem() #removing last inserted key-value pair
print(my_dict)
