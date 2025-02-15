def sortRGB(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 'R':
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 'G':
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Input array (you can also replace this with user input if needed)
input_array = ['R', 'R', 'G', 'G', 'G', 'G', 'B', 'B', 'B']
# Sorting the array
output_array = sorted(sortRGB(input_array))
# Print the input and output in the requested format
print(f"Output: [{','.join(output_array)}]")
