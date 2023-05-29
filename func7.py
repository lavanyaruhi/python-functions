from functools import cmp_to_key

def custom_compare(a, b):
    # Custom comparison logic
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

# Create a key function from the comparison function
key_func = cmp_to_key(custom_compare)

# Use the key function with sorted()
data = [5, 3, 9, 1, 7]
sorted_data = sorted(data, key=key_func)
print(sorted_data)
