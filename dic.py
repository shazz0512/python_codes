# key=['one', 'two', 'three','four', 'five']
# value=[1,2,3,4,5]
# return_dic=zip(key,value)
# print(dict(return_dic))

# dict_1={'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# dict_2={'red': 'rose', 'yellow': 'hibiscus'}
# print(dict_2['red'])
# dict_3=dict_1.copy()
# dict_3.update(dict_2)
# print(dict_3)
def dict_display_capitals(capitals): 
      print(capitals)
      
def dict_add_element(capitals):
       capitals={'Australia':'sydney'}
       print(capitals)
def dict_add_elements(capitals):
    
    capitals.update({ "India":"New Delhi","pakistan":"islamabad","Bangladesh":"dhaka"})
    print(capitals)
        
def dict_remove_element(capitals):
     print(capitals.pop("India"))

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
	
    capitals= {}
    for dict_elem in input('for ex:Nepal : Kathmandu, Ukraine :  Kyiv \n').split(","):
        temp_list = dict_elem.split(":")
        capitals[temp_list[0].replace('"','').strip()] = temp_list[1].replace('"','').strip()

    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display number of elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

my_dict_store()

