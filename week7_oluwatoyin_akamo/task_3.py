"""Function that return a new list of 
   distinct element from the first list"""
def dst_element(number):
    dst_list = []
    for num in number:
        if num not in dst_list:
            dst_list.append(num)
    return dst_list

# Test of the function
rand_list = [1,1,1,2,2,3,1,1,2,2,1,1,2,3]
order = dst_element(rand_list)
print(order)

rand_list2 = [1,2,2,3,3,3,1,1,7,4,5,6,8,8,8,9]
order2 = dst_element(rand_list2)
print(order2)
