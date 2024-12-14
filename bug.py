def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # Correct handling of division by zero
    else:
        return b / a

result = function_with_uncommon_error(0, 10)
print(result) # Output: 0

result = function_with_uncommon_error(10,0)
print(result) # Output: ZeroDivisionError: division by zero