from math import sqrt

def count_single_representation_pythagorean_triplets(max_value):
    triplet_count = [0]*(max_value + 1)
    max_m = int(sqrt(max_value))
    ab_values = set()
    for m in range(1, max_m + 10):
        for n in range(1, m):
            multiple = 1
            while True:
                a = multiple*(m*m - n*n)
                b = multiple*2*m*n
                perimeter = multiple*2*m*(m+n)
                ab = (a, b)
                if perimeter > max_value:
                    break
                if (a, b) not in ab_values and (b, a) not in ab_values:
                    ab_values.add(ab)
                    triplet_count[perimeter] += 1
                multiple += 1
    return len(filter(lambda c: c == 1, triplet_count))

if __name__ == "__main__":
    #print count_single_representation_pythagorean_triplets(48)
    print count_single_representation_pythagorean_triplets(1500000)
