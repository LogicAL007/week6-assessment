def distinct_elements(input_list):
    return set(input_list)

original_list = [1, 2, 2, 3, 4, 4, 5]
new_list = distinct_elements(original_list)
print(f"Original list: {original_list}")
print(f"List with distinct elements: {new_list}")
