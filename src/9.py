from math import sqrt

def is_int(x):
    return int(x) == x

def find_triplet(perimeter):
    for a in range(1, perimeter):
        a2 = a*a
        for b in range(a + 1, perimeter):
            c2 = a2 + b*b
            c = sqrt(c2)
            current_perimeter = a + b + c
            if current_perimeter > 1000:
                break
            if is_int(c):
                if current_perimeter == perimeter:
                    return (a, b, c)

if __name__ == "__main__":
    a, b, c = find_triplet(1000)
    print a * b * c
