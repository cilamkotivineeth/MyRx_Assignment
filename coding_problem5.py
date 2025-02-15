# Function to sort hashmap by value
def sort_map_by_value(input_map):
    sorted_map = dict(sorted(input_map.items(), key=lambda item: item[1]))
    return sorted_map

# Input hashmap
input_map = {101: 'John Doe', 102: 'Jane Smith', 103: 'Peter Johnson'}

# Sorting the hashmap by value
sorted_map = sort_map_by_value(input_map)

# Printing the sorted hashmap
print(sorted_map)
