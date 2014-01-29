from math import sqrt
import sys

def is_pentagonal(number):
    root = (1 + sqrt(1 + 24*number))/6
    return root == int(root)

def find_pentagonal_pair():
    min_difference = sys.maxint
    n1 = 1
    while True:
        for n2 in xrange(n1 - 1, 0, -1):
            p1 = (n1*(3*n1 - 1))/2
            p2 = (n2*(3*n2 - 1))/2
            difference = p1 - p2
            if difference > min_difference:
                break
            if is_pentagonal(difference) and is_pentagonal(p1 + p2):
                if difference < min_difference:
                    min_difference = p1 - p2
                    print n1, p1, p2, min_difference
        if min_difference < 3*n1 + 2:
            return min_difference
        n1 += 1

if __name__ == "__main__":
    print find_pentagonal_pair()

