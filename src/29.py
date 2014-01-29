import euler

if __name__ == "__main__":
    number = 2
    total_sum = 0
    while number < 1000000:
        digit_sum = 0
        for digit in euler.digits(number):
            digit_sum += digit**5
        if digit_sum == number:
            print number
            total_sum += number
        number += 1
print "->", total_sum
