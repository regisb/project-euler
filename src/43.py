import euler

def substring_divisible_numbers():
    number = 1234567890
    numbers = []
    permutations = euler.digit_permutations(number)
    for permutation in permutations:
        digits = euler.digits(permutation)
        if len(digits) < 10:
            digits.insert(0, 0)
        if euler.make_number(digits[1:4]) % 2 == 0 and\
            euler.make_number(digits[2:5]) % 3 == 0 and\
            euler.make_number(digits[3:6]) % 5 == 0 and\
            euler.make_number(digits[4:7]) % 7 == 0 and\
            euler.make_number(digits[5:8]) % 11 == 0 and\
            euler.make_number(digits[6:9]) % 13 == 0 and\
            euler.make_number(digits[7:10]) % 17 == 0:
            print permutation
            numbers.append(permutation)
    return numbers

if __name__ == "__main__":
    all_numbers = substring_divisible_numbers()
    print all_numbers, len(all_numbers), sum(all_numbers)
