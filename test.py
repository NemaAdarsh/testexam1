numbers = [1, 2, 3, 4, 5, 6]
target = 3

result = linear_search(numbers, target)

if result == -1:
    print("Target not found in list.")
else:
    print("Target found at index:", result)
def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i

    return -1
