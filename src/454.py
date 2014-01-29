#! /usr/bin/env python
import argparse

def count_solutions(L):
    count = 0
    for y in range(1, L+1):
        for x in range(1, y):
            if x*y % (x+y) == 0:
                count += 1
                n = x*y / (x+y)
                print "%d) x=%d y=%d n=%d" % (count, x, y, n)
    return count

def count_solutions_cumulated(L):
    count = 0
    for y in range(1, L+1):
        for x in range(1, y):
            if x*y % (x+y) == 0:
                count += 1
                #n = x*y / (x+y)
                #print "%d) x=%d y=%d n=%d" % (count, x, y, n)
        print count

def count_solutions_2(L):
    count = 0
    for x in range(1, L):
        for n in range(1, x):
            y = x*n*1. / (x-n)
            if y > L:
                break
            if y > x and x*n % (x-n) == 0:
                count += 1
                #print "%d) x=%d y=%d n=%d" % (count, x, y, n)
    return count


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Problem #454")
    parser.add_argument("L", type=int, help="L value")
    args = parser.parse_args()

    print count_solutions(args.L)
    #print count_solutions_2(args.L)
    #count_solutions_cumulated(args.L)
