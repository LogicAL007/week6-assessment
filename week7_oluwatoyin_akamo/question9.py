# write random functions that have args

def addition(*args):
    sum_numbers = 0
    for num in args:
        sum_numbers += num
    return sum_numbers


print(addition(2,7,9,8))