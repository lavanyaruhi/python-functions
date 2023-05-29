from functools import wraps

# Define a decorator to print function details
def print_details(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@print_details
def greet(name):
    """Greet a person."""
    print(f"Hello, {name}!")

greet("John")  # Output: Hello, John!
print(greet.__name__)  # Output: greet
print(greet.__doc__)  # Output: Greet a person.
