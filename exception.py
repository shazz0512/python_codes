try:
    # code that might raise an exception
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} / {num2} = {result}")
except ValueError:
    # handle a ValueError exception (e.g., if the user enters a non-numeric value)
    print("Error: Please enter a valid number")
except ZeroDivisionError:
    # handle a ZeroDivisionError exception (e.g., if the user enters 0 as the second number)
    print("Error: Cannot divide by zero")
except Exception as e:
    # handle all other exceptions
    print(f"Error: {e}")
finally:
    # code that will always execute, regardless of whether an exception was raised
    print("Thank you for using the program!")
