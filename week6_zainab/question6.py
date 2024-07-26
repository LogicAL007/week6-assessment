age1 = 10
age2 = 3
age3 = 1
age4 = 6

youngest = age3
#if and elif
if age1 < youngest:
    youngest = age1
elif age2 < youngest:
    youngest = age2
if age4 < youngest:
    youngest = age4
print(youngest)
