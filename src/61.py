import euler
from collections import defaultdict

def get_range(function, min_value, max_value):
    n = 0
    value = function(n)
    while value < min_value:
        n += 1
        value = function(n)
    results = []
    while value < max_value:
        results.append(value)
        n += 1
        value = function(n)
    return results

def triangle_numbers():
    return get_range(lambda n: (n*(n+1))/2, 1000, 10000)

def square_numbers():
    return get_range(lambda n: n*n, 1000, 10000)

def pentagonal_numbers():
    return get_range(lambda n: (n*(3*n-1))/2, 1000, 10000)

def hexagonal_numbers():
    return get_range(lambda n: n*(2*n-1), 1000, 10000)

def heptagonal_numbers():
    return get_range(lambda n: (n*(5*n-3))/2, 1000, 10000)

def octagonal_numbers():
    return get_range(lambda n: n*(3*n-2), 1000, 10000)

def get_suffix(number):
    return number % 100

def get_prefix(number):
    return euler.make_number(euler.digits(number)[:2])

def make_prefix_index(numbers):
    index = defaultdict(list)
    for number in numbers:
        prefix = get_prefix(number)
        index[prefix].append(number)
    return index

def find_path(prefix_indexes, first_prefix, required_prefix, processed_indexes):
    for prefix_position, prefix_index in enumerate(prefix_indexes):
        if prefix_position not in processed_indexes:
            if required_prefix in prefix_index:
                processed_indexes.add(prefix_position)
                for number in prefix_index[required_prefix]:
                    number_suffix = get_suffix(number)
                    if len(processed_indexes) < len(prefix_indexes):
                        result = find_path(prefix_indexes, first_prefix, number_suffix, processed_indexes)
                        if result is not None:
                            return [number] + result
                    elif number_suffix == first_prefix:
                        return [number]# WOOOOT!
                processed_indexes.remove(prefix_position)

def cyclical_figurate_numbers():
    polygonal_numbers = [triangle_numbers(), square_numbers(), pentagonal_numbers(), hexagonal_numbers(), heptagonal_numbers(), octagonal_numbers()]
    polygonal_indexes = map(make_prefix_index, polygonal_numbers)
    for prefix in range(10, 100):
        processed_indexes = set()
        path = find_path(polygonal_indexes, prefix, prefix, processed_indexes)
        if path is not None:
            print processed_indexes
            return path

cycle = cyclical_figurate_numbers()
print cycle, sum(cycle)
