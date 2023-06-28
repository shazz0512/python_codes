class Person:
    
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def intro(self):
        print(f"My name is {self.name} and i am {self.age} years old ")
        
class Student():
    
    def __init__(self,college_name,department):
        self.college_name=college_name
        self.department=department
        
    def mid(self) :
        print(f"My college name is {self.college_name} and i am from {self.department} department ") 
        
class Eng_Student(Person,Student):
    
    def __init__(self, name, age,college_name,department,year):
        Person.__init__(self,name, age)
        Student.__init__(self,college_name,department) 
        self.year=year
        
    def enroll(self):
        print(f"I am enrolled in {self.department} dpartment in the year {self.year} ")
        
s= Eng_Student("Kalpana", 23,"DPU","Computer",2023)
s.intro()
s.mid()
s.enroll()            
                            
        