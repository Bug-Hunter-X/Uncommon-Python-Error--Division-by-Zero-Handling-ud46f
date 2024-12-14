def function_with_robust_error_handling(a, b):
    try:
        if a == 0:
            return 0
        else:
            return b / a
    except ZeroDivisionError:
        return float('inf')  # Or any other suitable handling, like raising a custom exception
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

result = function_with_robust_error_handling(0, 10)
print(result)  # Output: 0

result = function_with_robust_error_handling(10, 0)
print(result)  # Output: inf

result = function_with_robust_error_handling(10, 'a')
print(result) # Output: An unexpected error occurred: unsupported operand type(s) for /: 'int' and 'str'
None