from functools import update_wrapper

def log_connection(func):
    def wrapper(*args, **kwargs):
        print(f"Establishing a connection...")
        result = func(*args, **kwargs)
        print("Connection closed.")
        return result

    # Update wrapper's attributes with attributes from the original function
    update_wrapper(wrapper, func)

    return wrapper

def send_data(host, port, data):
    print(f"Sending data to {host}:{port} - {data}")

# Usage
wrapped_send_data = log_connection(send_data)

wrapped_send_data("example.com", 80, "Hello, world!")
