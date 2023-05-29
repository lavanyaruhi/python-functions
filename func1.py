from functools import partial

# Define a function that adds two numbers
def add_numbers(a, b):
    return a + b

# Create a new function with the first argument fixed
add_five = partial(add_numbers, 5)

# Call the partially applied function
result = add_five(3)
print(result)  # Output: 8



#print(result)




