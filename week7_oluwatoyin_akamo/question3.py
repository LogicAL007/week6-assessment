#  Write a Python function that takes a list and returns a new list with
# distinct elements from the first list.

def unique_list(numbers):
    unique = []
    for item in numbers:
        if item not in unique:
            unique.append(item)
    return unique


print(unique_list([2,2,5,5,3,3,1,1,4,4,8,8,7,7,7]))