# Write a Python function to check whether a number falls within a
# given range

def my_range(number):
   start = 3
   end = 9
   if number >= start and number <= end:
       return True
   else:
       return False


number = 5
is_in_range = my_range(number)
print(f"The number {number} is in the range: {is_in_range}")