
#     # initialize an empty dictionary to store student details
# student_dict = {}

# # get the number of students from the user
# num_students = int(input("Enter the number of students: "))

# # loop through each student and get their details
# for i in range(num_students):
#     print(f"Enter details for student {i+1}:")
#     name = input("Name: ")
#     age = input("Age: ")
#     address = input("Address: ")
#     # store the details in a dictionary for each student
#     student_dict= {'name': name,'age': age, 'address': address}

# # print the final dictionary of student details
# print("\nStudent details:")
# print(student_dict)


dict={}
for i in range(2):
    name=input("name: ")
    prn=int(input("PRN: "))
    collage=input("collage name: ")
    place=input("place: ")
    dict[name]=prn
    dict[collage]=place
print("\n STUDENT DETAILS:")    
print(dict)    


# write the dictionary to a file
def write():
 with open('student_detail.txt', 'w') as file:
    for key, value in dict.items():
        file.write(f"{key}: {value}\n")
def read():   
 with open('student_detail.txt', 'r') as file:
     return_str=file.read()
     print(return_str)
write()
read()     