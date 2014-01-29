def is_pandigital(number_string):
    if len(number_string) != 9:
        return False
    digits = [False]*10
    for digit_string in number_string:
        digit = int(digit_string)
        if digit == 0 or digits[digit]:
            return False
        digits[digit] = True
    return True

def largest_pandigital():
    max_pandigital = 0
    for number in range(1, 10000):
        number_string = str(number)
        multiplier = 2
        while len(number_string) < 9:
            number_string += str(number*multiplier)
            multiplier += 1
        if is_pandigital(number_string):
            max_pandigital = max(max_pandigital, int(number_string))
    return max_pandigital

if __name__ == "__main__":
    print(largest_pandigital())
