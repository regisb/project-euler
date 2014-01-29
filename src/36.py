import euler

def is_palindrome(digits):
    for index in range(0, len(digits)/2):
        if digits[index] != digits[-index - 1]:
            return False
    return True

def double_base_palindromes(max_value):
    palindromes = []
    for number in range(0, max_value):
        decimal_digits = euler.digits(number)
        if is_palindrome(decimal_digits):
            binary_digits = euler.binary_digits(number)
            if is_palindrome(binary_digits):
                palindromes.append(number)
    return palindromes

if __name__ == "__main__":
    print euler.binary_digits(0)
    print euler.binary_digits(1)
    print euler.binary_digits(2)
    print euler.binary_digits(3)
    print euler.binary_digits(4)
    palindromes = double_base_palindromes(1000000)
    print palindromes, sum(palindromes)
