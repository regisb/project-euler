from math import sqrt

def digit_count(number):
    return len(str(number))
    #max_value = 10
    #digit_count = 1
    #while True:
        #if number < max_value:
            #return digit_count
        #digit_count += 1
        #max_value *= 10

def digits(number):
    digits = []
    while number >= 10:
        digits.append(number % 10)
        number /= 10
    digits.append(number)
    return list(reversed(digits))

def binary_digits(number):
    digits = []
    while number > 0:
        digits.insert(0, number%2)
        number = number // 2
    return digits

def make_number(digits):
    number = 0
    factor = 1
    for pos in range(len(digits) - 1, -1, -1):
        number += factor * digits[pos]
        factor *= 10
    return number

def digit_permutations(number):
    return _digit_permutations(digits(number))

def _digit_permutations(digits):
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return [digits[0]]
    processed_digits = [False]*10
    permutations = []
    for digit_position, digit in enumerate(digits):
        if processed_digits[digit]:
            continue
        offset = digit * 10**(len(digits) - 1)
        partial_digits = digits[:digit_position] + digits[digit_position+1:]
        partial_permutations = _digit_permutations(partial_digits)
        for permutation in partial_permutations:
            permutations.append(permutation + offset)
        processed_digits[digit] = True
    return permutations

def digit_rotations(number):
    number_digits = digits(number)
    rotations = set()
    for _ in range(0, len(number_digits)):
        number_digits.insert(0, number_digits.pop())
        rotations.add(make_number(number_digits))
    return list(rotations)

def string_digits(text):
    return [ord(character) - 96 for character in text.lower()]

def string_value(text):
    return sum(string_digits(text))

def is_triangular(number):
    root = (-1 + sqrt(1 + 8*number))/2
    return root == int(root)

def is_pentagonal(number):
    root = (1 + sqrt(1 + 24*number))/6
    return root == int(root)

def is_hexagonal(number):
    root = (1 + sqrt(1 + 24*number))/4
    return root == int(root)

def argmin(function, arg_values):
    min_result = None
    arg_min = None
    for arg in arg_values:
        result = function(arg)
        if result < min_result or arg_min is None:
            min_result = result
            arg_min = arg
    return arg_min

def argmax(function, arg_values):
    max_result = None
    arg_max = None
    for arg in arg_values:
        result = function(arg)
        if result > max_result or arg_max is None:
            max_result = result
            arg_max = arg
    return arg_max
