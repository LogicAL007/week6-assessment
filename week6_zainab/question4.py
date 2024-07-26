enter_year = int(input("enter the year"))

if (enter_year%4) ==0:
    if(enter_year%100) ==0:
        if(enter_year%400) ==0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
    else:
        print("This is a leap year")
else:
    print("This is not a leap year")


