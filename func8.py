from functools import reduce
packets = [
    {'packet_id': 1, 'size': 100},
    {'packet_id': 2, 'size': 200},
    {'packet_id': 3, 'size': 300},
    ]
total_size = reduce(lambda a, b: a + b['size'], packets)
print(total_size)
