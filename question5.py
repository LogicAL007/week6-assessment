#task 5
def oldest_person_age():
    abc1 = int(input("Enter age1: "))
    abc2 = int(input("Enter age2: "))
    abc3 = int(input("Enter age3: "))
    abc4 = int(input("Enter age4: "))

    oldest_age = max(abc1, abc2, abc3, abc4)
    print("The oldest persons age is", oldest_age)
oldest_person_age()