def my_list():
    print("\n Welcome to our lists")
    print("please enter the list comma separated that you would want to perform")
    members = input('eg. preeti,sonu \n').split(",")
    
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("  1:  Display number of elements in the members list")
        print("  2:  Add an element to the members collection like 'Sehwag' ")
        print("  3:  Add elements to the members collection like ['David','Bret','Sanju']")
        print("  4:  Remove a member from the collection at a given subscript")
        print("  5:  Remove the last member from the collection ")
        print("  6:  Display third, fourth and fifth element from the collection ")
        print("  7:  Display reverse string ")
        print("  8: Exit the Program ")
    
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            list_display_members(members) 
        elif choice ==2:
            list_add_element(members) 
        elif choice ==3:
            list_add_elements(members)
        elif choice ==4:
            list_remove_element(members) 
        elif choice ==5:
            remove_last_element(members) 
        elif choice ==6:
            display_3_4_5_element(members) 
        elif choice ==7:
            display_reverse_element(members) 
        elif choice ==8: 
            break   
        else:
            print("Invalid Input , Please Try Again !!!!  ")
     
     
     
     
def list_display_members(members):
    print(members)
    
def list_add_element(members):
    members.append(input("Enter the name  "))  
    

def list_add_elements(members):
     members.extend(input("Enter the names ").split(","))   
   
     
def list_remove_element(members):
    members.pop(int(input("Enter the index "))) 
   
    
def remove_last_element(members) :
    members.pop()
     
def display_3_4_5_element(members) :
    if len(members)<=5:
        print("you dont have enough members, please add to list "   )
        list_add_elements(members)
    else:
     print( members[3] )  
     print( members[4] )  
     print( members[5] )  
     
def display_reverse_element(members) : 
     members.reverse() 
     list_display_members(members)   
    
    
my_list()