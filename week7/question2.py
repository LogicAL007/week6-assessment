def detect_case():
    n= '''("Malaria is a common illness in Nigeria. It is caused by a parasite called Plasmodium Spp
    Its affects both male and female"): '''
    count_lower = 0
    count_upper = 0
    for i in n:
        if i.isupper():
            count_upper+=1
        elif i.islower():
            count_lower+=1

    return count_upper, count_lower
print (detect_case())



