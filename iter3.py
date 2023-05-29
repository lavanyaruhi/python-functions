import itertools

# Sample network traffic data
traffic_data = [
    {'source': '192.168.0.1', 'destination': '10.0.0.1', 'protocol': 'TCP', 'port': 80, 'bytes': 1500},
    {'source': '10.0.0.2', 'destination': '192.168.0.1', 'protocol': 'UDP', 'port': 5000, 'bytes': 1200},
    # Add more traffic data...
]

# Group traffic data by source IP address
traffic_by_source = itertools.groupby(traffic_data, key=lambda x: x['source'])

# Calculate total bytes sent by each source IP address
bytes_by_source = {}
for source, traffic in traffic_by_source:
    total_bytes = sum(entry['bytes'] for entry in traffic)
    bytes_by_source[source] = total_bytes

# Sort the sources based on total bytes in descending order
sorted_sources = sorted(bytes_by_source.items(), key=lambda x: x[1], reverse=True)

# Print the sources and their total bytes
for source, total_bytes in sorted_sources:
    print(f"Source: {source}, Total Bytes: {total_bytes}")
