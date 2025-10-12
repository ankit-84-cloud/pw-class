#creating Strings

str1 = "Hello"
str2 = 'World'
str3 = """
This is a
multiline string.
"""
print(str3)

#String Concatenation
greeting = str1 + " " + str2
print(greeting)
#f string to print multiple variables
print(f"{str1} {str2} {str3}")

## repeating strings
print((str1 + " ") * 3)

 

 ##string slicing
print(str1[0:4])  # Hell
print(str2[2:])  # llo

#string length

print(f"Length of str1: {len(str1)}")

# change case
print(f"Uppercase: {str1.upper()}")
print(f"Lowercase: {str2.lower()}")

#replace
print(str1.replace("H", "w"))  # Jello

## search
print ("lo" in str1)  # True # check if its presentin str or not

## split and join
statement="my name is ankit kashyap and i am a developer"
words=statement.split(" ")
print(words)   # array or all words
print("-".join(words))  # join with -

## check start with and ends with
print("python".startswith("py"))  # True
print("python".endswith("on"))  # True

#statements
# write logic to captalize first letter of each word in a stringre

result=""
for i in words:
    result+= i.capitalize(

    ) + " "
print(result)

#center
text="python"
print(text.center(30, "*"))

##Another way

result = " ".join(word[0].upper() + word[1:] for word in statement.split(" "))
print(result)