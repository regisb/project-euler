def find_permutable_multiples():
    number = 1
    while True:
        set1 = set(str(number))
        set2 = set(str(2*number))
        set3 = set(str(3*number))
        set4 = set(str(4*number))
        set5 = set(str(5*number))
        set6 = set(str(6*number))
        if set1 == set2 and set1 == set3 and set1 == set4 and set1 == set5 and set1 == set6:
            return number
        number += 1

print find_permutable_multiples()
