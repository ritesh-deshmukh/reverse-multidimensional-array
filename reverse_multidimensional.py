# Write some code (including tests) that will reverse an array of
# arbitrary elements in place along with any arrays (or  arrays ofarrays).
# For example: [1, 2, [3, 4, 5], [6, [7, 8], 9]] => [[9, [8, 7], 6], [5, 4, 3], 2, 1]


arr = [1, 2, [3, 4, 5], [6, [7, 8], 9]]


def reverse_main(arr):
    # recursive function
    return [(reverse_main(x) if check_type(x) else x)
                             for x in reverse_list(arr)]


# check if type is list or int
# if list, reverse further
def check_type(x):
    if type(x) is list:
        return True
    else:
        return


# controller to reverse a list
def reverse_list(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr

# Print output
# print(f"Given array: {arr}")
# print(f"Reversed array: {reverse_main(arr)}")
