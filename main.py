def sum(a, b):
    try:
        return a + b
    except ValueError:
        print("Error: Invalid value provided.")
    except TypeError:
        print("Error: Both arguments must be numbers.")
    except NameError:
        print("Error: One or both variables are not defined.")  
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 
    return None 
# Example usage with valid inputs
print(sum(5, 10))  # Should print 15
# Example usage with a TypeError
print(sum(5, '10'))  # Should print an error message
# Example usage with a NameError
print(sum(5, c))  # Should print an error message   # where 'c' is not defined 
# Example usage with a ValueError (not directly applicable here, but included for completeness)
print(sum(5, None))  # Should print an error message  


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both arguments must be numbers.")
    except NameError:
        print("Error: One or both variables are not defined.")  
    except Exception as e:
        print(f"An unexpected error occurred: {e}") 
    return None
# Example usage with valid inputs
print(divide(10, 2))  # Should print 5.0
# Example usage with a ZeroDivisionError
print(divide(10, 0))  # Should print an error message
# Example usage with a TypeError
print(divide(10, '2'))  # Should print an error message
# Example usage with a NameError
print(divide(10, d))  # Should print an error message   # where 'd' is not defined 
# Example usage with a ValueError (not directly applicable here, but included for completeness)
print(divide(10, None))  # Should print an error message    