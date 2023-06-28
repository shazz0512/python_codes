# define a string variable
string = "hello world"

# print the original string
print("Original string:", string)

# convert the string to uppercase
uppercase_string = string.upper()
print("Uppercase string:", uppercase_string)

# convert the string to lowercase
lowercase_string = string.lower()
print("Lowercase string:", lowercase_string)

# count the number of occurrences of a substring
substring = "l"
count = string.count(substring)
print(f"Number of '{substring}' in string: {count}")

# check if a substring is present in the string
if "world" in string:
    print("Substring 'world' found in string")
else:
    print("Substring not found")

# replace a substring with another string
new_string = string.replace("world", "Python")
print("New string:", new_string)

# split the string into a list of substrings
split_string = string.split()
print("Split string:", split_string)



# create two strings
string1 = "Hello"
string2 = "world"

# concatenate the two strings
string3 = string1 + " " + string2
print("Concatenated string:", string3)

# slice a substring from the original string
substring = string1[1:4]
print("Sliced substring:", substring)

# format a string with variables
name = "Alice"
age = 30
greeting = "My name is {} and I am {} years old.".format(name, age)
print("Formatted string:", greeting)

































