import itertools
import random

def generate_ip_addresses():
    octets = [range(1, 256)] * 4  # Generate four octets for the IP address
    ip_addresses = ('.'.join(map(str, address)) for address in itertools.product(*octets))
    return ip_addresses

def assign_ip_addresses(num_servers, num_receivers):
    ip_pool = list(generate_ip_addresses())
    random.shuffle(ip_pool)  # Shuffle the IP addresses randomly

    dhcp_servers = ip_pool[:num_servers]
    dhcp_receivers = ip_pool[num_servers:num_servers+num_receivers]

    return dhcp_servers, dhcp_receivers

# Specify the number of DHCP servers and receivers
num_dhcp_servers = 3
num_dhcp_receivers = 10

# Assign IP addresses to DHCP servers and receivers
servers, receivers = assign_ip_addresses(num_dhcp_servers, num_dhcp_receivers)

# Print the assigned IP addresses for DHCP servers
print("DHCP Servers:")
for i, server in enumerate(servers):
    print(f"Server {i+1}: {server}")

# Print the assigned IP addresses for DHCP receivers
print("\nDHCP Receivers:")
for i, receiver in enumerate(receivers):
    print(f"Receiver {i+1}: {receiver}")
