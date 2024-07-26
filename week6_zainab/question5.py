age1 = 25
age2 = 32
age3 = 40
age4 = 56

oldest = age4
# if and elif
if age1 > oldest:
    oldest = age1
elif age2 > oldest:
    oldest = age2
if age3 > oldest:
    oldest = age3
print(oldest)
