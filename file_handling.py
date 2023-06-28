# def write():
#     file_create=open("ab.txt", "at+")
#     my_str="Hello love you can do it"
#     file_create.write(my_str+"\n")
#     file_create.close()
# def read():
#     file_read=open("ab.txt", "rt+")
#     return_str=file_read.read()
#     print(return_str) 
#     file_read.close()

# write()
# read()


"""this code contains the file handling demo"""

# def file_write():
#     file_create=open("abc.txt","at+")
#     my_str="Hello this is demo file, created using python"
#     file_create.write(my_str+"\n")
#     file_create.close()
     
# def file_read():
#     file_created_read=open("abc.txt","rt+")
#     return_str=file_created_read.read()
#     print(return_str)
#     file_created_read.close()
    

# file_read()


# def write():
#     file_create=open("ab1.txt","at+")
#     my_str="hello you will definately win"
#     file_create.write(my_str+"\n")
#     file_create.close()
# def read():
#     file_read=open("ab1.txt","rt+")
#     return_str=file_read.read()
#     print(return_str)
#     file_read.close()
    
    
# write()
# read()    


def write():
 with open('sample.txt',"w") as file:
    str="HELLO, I am from DHPCSA"
    file.write(str+"\n")
    
def read():
    with open('sample.txt',"r+") as file:
     return_str=file.read() 
     print(return_str)   

write()
read()    