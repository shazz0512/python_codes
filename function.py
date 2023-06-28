# def area_of_circle(radius):
#     area= 3.14 * radius **2
#     return area

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# radius=20
# area=area_of_circle(radius) 
# print(f"The area of a circle with radius {radius} is {area}")  

# n=6
# factorial= factorial(n)
# print(f"The factorial of {n} is {factorial}")




# function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

#take user input and check if it's prime
num = int(input("Enter a number to check if it's prime: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")
