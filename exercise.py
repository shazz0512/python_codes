# Print th sum of "n" natural numbers using the whie loop AND for loop

# n=10
# sum=0
# while n<11 :
#     sum = n*(n+1)/2                             #PRINTS THE SUM OF NUMBER TILL PARTICULAR UPPERBOUND
#     print(sum)
#     n += 1
#     break
    

# n=int(input("Enter the number "))
# sum=0
# for i in range (1,n+1,1) :                      #PRINTS THE SUM FOR ANY GIVEN NUMBER
#     sum = n*(n+1)/2
#     print(sum)              
#     break



# calculte the averge of the given numbr

# n=int(input("Enter the number  "))
# sum=0
# avg=0
# for i in range(1,n+1):
#     sum = n*(n+1) / 2
#     avg= sum / n
#     print("Sum of the number is  ",sum)
#     print("Average of the number is  ",avg)
#     break


#PRINT MULTIPLICATION TABLE OF THE GIVEN NUMBER

# N = int(input("Enter the number  "))
# cnt=0
# for i in range(1,11,1):
#     sum=N*i
#     print(sum)
#     cnt += 1
    

# Display numbers from a list using loop
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

# N = [1,15,60,545,160,40] 
# print (N)
# for item in N:
#     if item > 500:
#       break
#     elif item > 150 :
#      continue
#     if item % 5 == 0:
#         print(item)
        
        
#Count the total number of digits in a number   

# number = 75869
# cnt=0
# while number != 0:
#     sum=  number // 10
    
#     cnt += 1   
#     print(cnt)
#     break

# num = 75869
# count = 0
# while num != 0:
#     # floor division
#     # to reduce the last digit from number
#     num = num // 10

#     # increment counter by 1
#     count = count + 1
# print("Total digits are:", count)



#Print list in reverse order using a loop


# list1 = [10, 20, 30, 40, 50]
# new_list = reversed(list1)
# for item in new_list:
#     print(item, end=(' '))
    

# list1 = [10, 20, 30, 40, 50]
# # get list size
# # len(list1) -1: because index start with 0
# # iterate list in reverse order
# # star from last item to first
# size = len(list1) - 1
# for i in range(size, -1, -1):
#     print(list1[i],end=(' '))


#Display numbers from -10 to -1 using for loop

# for i in range(-10,0,1):
#     print(i)
# else:
#     print("Done!!") 



#Write a program to display all prime numbers within a range

# upperbound=int(input("Enter the from which no you wnt to search "))
# lowerbound=int(input("Enter the till which no you wnt to search "))
# for num in range(upperbound, lowerbound + 1):
#     # all prime numbers are greater than 1
#     # if number is less than or equal to 1, it is not prime
#     if num > 1:
#         for i in range(2, num):
#             # check for factors
#             if (num % i) == 0:
#                 # not a prime number so break inner loop and
#                 # look for next number
#                 break
#         else:
#             print(num,end=(' '))        
            
            
            
#Display Fibonacci series up to 10 terms
# a=-1
# b=1
# cnt = 0
# n=int(input("Enter the number "))
# for i in range(2,n+1):
#     sum = a+b
#     print (sum,end=(' '))
#     a=b
#     b=sum
#     cnt +=  1            


#Find the factorial of a given number

# n=int(input("Enter the number "))
# fact = 1
# if n<0:
#     print("We cant remove fctorial of negative no ")
# elif n== 0:
#     print("Fatorial of zero is one")
# else:
#     for i in range(1,n+1) :
#         fact=fact*i 

#         print(fact,end=' ')  
        
"""Take a number from the user and print all prime numbers from 1 to that number """

# def isprime_no(n):
#     if n == 1 or n == 0:
#         return False
    
#     for i in range(2,int(num**0.5)+1):     # for i in range(2,(n//2)+1):                                      """
#         if (n % i == 0):
#             return False
    
    
#     else:
#         return True
    
# num=int(input("Enter the no "))    
# for i in range(1,num+1) :
#     if (isprime_no(i)):
#         print(i,end=' ')
        
 
 
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  
# print(my_list)
# for i in my_list[::-1] :
#     print(i,end=' ')
      
      
      

# n=int(input("Enter the number ")) 
# for i in range(1,n+1,1):
#     cube= i*i*i

#     print("Current number is ",i "Cube is ",cube ,end=" ")   




# program to swap the first and last elements in the list   

# def swap(list):
#     if len(list)<2:
#         return list
#     else:
#         first_elem=list[0]
#         last_elem=list[-1]
#         list[0]=last_elem
#         list[-1]=first_elem
#         return list
    
# my_list=(input("enter the elements with comma seperated ")).split(",")
# print(type(my_list))
# print("Before swap: ",my_list)
# print("After swap: ",swap(my_list))  



def odd_even(n):
 for i in range(1): 
    if n % 2 == 0:
      return True
    else:
        return False
        
  #odd even function program
   
n=int(input('Entr the no '))
# for i in range(1,n+1):
#     if odd_even(i):
#         print(i, end=' ')
if odd_even(n):
    print(f'{n} is even no')
else:
   print(f'{n} is odd no')  

 
# Fibonnaci series

# a=-1
# b=1
# cnt=0
# n=int(input('Entr the no '))
# for i in range(2,n+1):
#     sum=a+b
#     print(sum,end=' ')
#     a=b
#     b=sum
#     cnt += 1


# Function to generate Fibonacci series up to a given number
# def fibonacci(n):
#     # Initialize the first two numbers of the series
#     a, b = 0, 1
#     # Loop until the current number is less than or equal to n
#     while a <= n:
#         # Print the current number in the series
#         print(a, end=' ')
#         # Update the values of a and b to generate the next number in the series
#         a, b = b, a + b

# # Get input from user
# n = int(input("Enter a number: "))
# # Call the fibonacci function to generate the series up to n
# fibonacci(n)

 



    










    