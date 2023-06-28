def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y
def sqr(x):
    return x**2
def expo(x,y):
    return x**y
    
def HOF(func,arg1,arg2=None):
    if arg2 is not None:
        return func(arg1,arg2) 
    else:
        return func(arg1)  
    
def my_calculator():             
        print("Enter your choice")
        print("1. Addition")
        print("2. Subtraction")
        print("3. multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Exponentation")
        ch=int(input("Enter your choice "))
        if ch ==1:
            num1=int(input("Enter 1st number: "))
            num2=int(input("Enter 2st number: "))
            return_var= HOF(add,num1,num2)
            print("Addition :", return_var)
        if ch ==2:
            num1=int(input("Enter 1st number: "))
            num2=int(input("Enter 2st number: "))
            return_var= HOF(sub,num1,num2)
            print("subtraction :", return_var)
        if ch ==3:
            num1=int(input("Enter 1st number: "))
            num2=int(input("Enter 2st number: "))
            return_var= HOF(mul,num1,num2)
            print("Multiplication :", return_var) 
        if ch ==4:
            num1=int(input("Enter 1st number: "))
            num2=int(input("Enter 2st number: "))
            return_var= HOF(div,num1,num2)
            print("Division :", return_var)           
        if ch ==5:
            num1=int(input("Enter number: "))
            return_var= HOF(sqr,num1)
            print("Square:", return_var)   
        if ch ==6:
            num1=int(input("Enter 1st number: "))
            num2=int(input("Enter 2st number: "))
            return_var= HOF(expo,num1,num2)
            print("Exponentation :", return_var)
        
            
def iterative_calculator():
    while(True):
        my_calculator()
        choice=input("Do you want to continue , press y/n: ").lower()
        if choice == 'n':
            break
        
        
iterative_calculator()        