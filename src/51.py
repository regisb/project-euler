from collections import defaultdict
import eratosthenes
import euler

def binary_string(number, digit_count):
    padded_number_string = bin(number)[2:]
    if len(padded_number_string) < digit_count:
        padding_length = digit_count - len(padded_number_string)
        padded_number_string = "0"*padding_length + padded_number_string
    return padded_number_string

def get_signature_indexes_from_string(signature_binary_string):
    indexes = []
    for position, signature_binary_digit in enumerate(signature_binary_string):
        if signature_binary_digit == "1":
            indexes.append(position)
    return indexes

def get_signature_indexes(signature_value, digit_count):
    signature_binary_string = binary_string(signature_value, digit_count)
    return get_signature_indexes_from_string(signature_binary_string)

def digits_match_signature(digits, signature_value):
    digit_count = len(digits)
    signature_indexes = get_signature_indexes(signature_value, digit_count)
    digit = digits[signature_indexes[0]]
    for signature_index in signature_indexes:
        if digits[signature_index] != digit:
            return False
    return True

def signature_remainder(digits, signature_value):
    remainder = ""
    signature_binary_string = binary_string(signature_value, len(digits))
    for digit, bit in zip(digits, signature_binary_string):
        if bit == "0":
            remainder += str(digit)
    if len(remainder) == 0:
        remainder = "0"
    return int(remainder)

def number_signature_remainder(number):
    digits = euler.digits(number)
    digit_count = len(digits)
    for signature_value in range(1, 2**digit_count):
        if digits_match_signature(digits, signature_value):
            remainder = signature_remainder(digits, signature_value)
            yield binary_string(signature_value, digit_count), remainder

def find_prime_digit_replacements(digit_count, match_count):
    signature_remainders = defaultdict(lambda: defaultdict(set))
    max_value = 10**digit_count
    min_value = 10**(digit_count - 1)
    eratosthenes.init(max_value)
    primes = set(eratosthenes.prime_range(min_value, max_value))
    for prime in primes:
        for signature, remainder in number_signature_remainder(prime):
            signature_remainders[signature][remainder].add(prime)
            if len(signature_remainders[signature][remainder]) >= match_count:
                intersection = signature_remainders[signature][remainder]
                print signature, remainder, sorted(intersection)
    #prime_signatures = defaultdict(list)
    #signatures = []
    #for prime in primes:
        #for signature

if __name__ == "__main__":
    find_prime_digit_replacements(6, 8)
