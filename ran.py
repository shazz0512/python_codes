# import random

# # generate a random number between 1 and 10 (inclusive)
# random_number = random.randint(1, 10)

# print(f"The random number is {random_number}")


# define two dictionaries
dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 25, 'c': 35, 'd': 45}

# print the dictionaries
print("Dictionary 1: ", dict1)
print("Dictionary 2: ", dict2)

# add the values of matching keys in the two dictionaries
dict_sum = {}
for key in dict1:
    if key in dict2:
        dict_sum[key] = dict1[key] + dict2[key]

# print the result
print("Dictionary sum: ", dict_sum)

# merge the two dictionaries
dict_merge = dict1.copy()
dict_merge.update(dict2)

# print the result
print("Dictionary merge: ", dict_merge)

# find the common keys in the two dictionaries
common_keys = set(dict1.keys()) & set(dict2.keys())

# print the result
print("Common keys: ", common_keys)
