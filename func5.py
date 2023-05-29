import socket
from functools import wraps

def log_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Establishing a connection to {args[0]}...")
        result = func(*args, **kwargs)
        print("Connection closed.")
        return result
    return wrapper

@log_connection
def send_data(host, port, data):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.sendall(data.encode())
    sock.close()

# Usage
send_data("example.com", 80, "Hello, world!")
