# Write a program that will ask the user for their height in centimeters.
# Use the input() built-in function to do this. If the height is more than
# 185 centimeters, print the following line of code: “You are very Tall”.

height = 185
user_height = int()
while True:
  user_height = int(input('Enter your height'))
  if user_height > height:
    print('You are very Tall')
    break
  else:
    print('You are not very Tall')