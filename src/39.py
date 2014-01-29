from math import sqrt

def is_int(x):
    return int(x) == x

def count_triplets(max_perimeter):
    perimeter_count = [0]*max_perimeter
    best_perimeter_count = 0
    best_perimeter = 0
    for a in range(1, max_perimeter):
        for b in range(a+1, max_perimeter - a):
            c = sqrt(a*a + b*b)
            if is_int(c):
                perimeter = a + b + int(c)
                if perimeter < max_perimeter:
                    perimeter_count[perimeter] += 1
                    if perimeter_count[perimeter] > best_perimeter_count:
                        best_perimeter = perimeter
                        best_perimeter_count = perimeter_count[perimeter]
    return best_perimeter

if __name__ == "__main__":
    print count_triplets(1001)
