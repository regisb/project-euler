import euler

def square_root_convergent_long_numerator_count():
    numerator = 3
    denominator = 2
    iteration = 1
    count = 0
    while iteration <= 1000:
        if len(euler.digits(numerator)) > len(euler.digits(denominator)):
            count += 1
        numerator_next = numerator + 2*denominator
        denominator = numerator + denominator
        numerator = numerator_next
        iteration += 1
    return count

print square_root_convergent_long_numerator_count()
