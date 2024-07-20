# Here, I defined the fucnction using the "def" function
def check_user_height_in_centimeters():

    # Here, i specified the variable "entered height", and created a prompt that will ask the user to enter their heights. 
    # Next, I used the 'int' function to convert the entered string, to an integer.
    entered_height = int(input("Please enter your height in centimeters: "))

    # Here, I used conditional operators to setup the conditions for the "if" and "else" statements
    if entered_height > 185:
        print("You are very tall.")
    else:
        print("you are good to go")

# Lastly, i called the function, to check the Heights, having set all conditions.
check_user_height_in_centimeters()

# Here, I decided to play around a bit with more works.
height = int(input("Enter your height in centimeters, with respect to your monthly salary in dolars: "))
txt = f"The price is {height} dollars"
if height >= 100:
    print("your height is as good as GOAL!!!!")
else:
    print("you need to look for a job with a better hourly pay")