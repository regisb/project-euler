def iter_digits(number):
    while number > 0:
        remainder = number % 10
        yield remainder
        number = (number - remainder)/10

def is_valid(number):
    count = [0]*10
    for digit in iter_digits(number):
        if digit == 0 and number < 1000000000:
            return False
        count[digit] += 1
        if count[digit] > 1:
            return False
    return True

number = 2987654310
count = 1088640
while count > 1000000:
    number -= 1
    if is_valid(number):
        count -= 1
        if count % 10000 == 0:
            print count, number
print number
