# error handling


"""x = int((input("Enter a number: ")))  # User input
y = int((input("Enter a number: ")))  # User input
result = x / y
print(f"Result: {result}")"""
# This will raise an error if y is 0 (ZeroDivisionError)
# This will raise an error if the input is not a number (ValueError)
# We can handle these errors using try-except blocks
try:
    x = int((input("Enter a number: ")))  # User input
    y = int((input("Enter a number: ")))  # User input
    result = x / y
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

