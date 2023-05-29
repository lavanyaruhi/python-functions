import itertools
import random

def generate_ip_addresses(start_ip, end_ip):
    start = list(map(int, start_ip.split('.')))
    end = list(map(int, end_ip.split('.')))

    # Generate IP addresses between the start and end range
    ip_pool = ['.'.join(map(str, address)) for address in itertools.product(range(start[0], end[0] + 1),
                                                                          range(start[1], end[1] + 1),
                                                                          range(start[2], end[2] + 1),
                                                                          range(start[3], end[3] + 1))]
    return ip_pool

def dhcp_server(ip_pool):
    while True:
        # Simulate DHCP lease allocation
        allocated_ip = random.choice(ip_pool)
        ip_pool.remove(allocated_ip)
        yield allocated_ip

def dhcp_client(dhcp_server):
    for _ in range(10):
        allocated_ip = next(dhcp_server)
        print(f"Allocated IP: {allocated_ip}")

# Define the IP address range for DHCP server
start_ip = '192.168.0.100'
end_ip = '192.168.0.200'

# Generate the IP address pool
ip_pool = generate_ip_addresses(start_ip, end_ip)

# Create a DHCP server and assign IP addresses
server = dhcp_server(ip_pool)

# Simulate DHCP clients requesting IP addresses
dhcp_client(server)
