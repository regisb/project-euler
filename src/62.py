from collections import defaultdict

def find_cubic_permutations():
    max_value = 100000
    cubic_permutations = defaultdict(list)
    for number in xrange(1, max_value + 1):
        cube = number**3
        cube_key = "".join(sorted(str(cube)))
        cubic_permutations[cube_key].append(cube)
        equivalence_cubes = cubic_permutations[cube_key]
        if len(equivalence_cubes) == 5:
            return equivalence_cubes

print find_cubic_permutations()
