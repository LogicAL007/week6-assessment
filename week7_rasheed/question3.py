def distinct_elements(input_list):
    distinct_elements = list(set(input_list))
    return distinct_elements

# Example
input_list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9]
distinct_list = distinct_elements(input_list)
print(f"Original list: {input_list}")
print(f"Distinct elements: {distinct_list}")