import itertools

def assign_ip_addresses(server_subnet, receiver_subnet, server_count, receiver_count):
    server_ips = (f"{server_subnet}.{i}" for i in itertools.islice(itertools.count(1), server_count))
    receiver_ips = (f"{receiver_subnet}.{i}" for i in itertools.islice(itertools.count(1), receiver_count))
    return zip(server_ips, receiver_ips)

# Assign IP addresses for DHCP server and receiver
server_subnet = "192.168.1"
receiver_subnet = "10.0.0"
server_count = 5
receiver_count = 10

assignments = assign_ip_addresses(server_subnet, receiver_subnet, server_count, receiver_count)

# Print the assigned IP addresses
for server_ip, receiver_ip in assignments:
    print(f"DHCP Server IP: {server_ip}, Receiver IP: {receiver_ip}")
