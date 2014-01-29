import euler

def numerator(q):
    return int(3*float(q)/7)

def left_of_three_seventh(q):
    return numerator(q)/float(q)

if __name__ == "__main__":
    denominators = filter(lambda q: q%7 != 0, xrange(1, 1000001))
    q = euler.argmax(left_of_three_seventh, denominators)
    print numerator(q), q

