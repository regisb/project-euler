
MAX_SIZE = 1000000

def dividers_count():
    dividers_count = [0]*(MAX_SIZE + 1)
    for number in range(1, MAX_SIZE):
        pos = number
        while pos < MAX_SIZE:
            dividers_count[pos] += 1
            pos += number
    return dividers_count

def first_triangle_number_with_over_500_dividers():
    n = 1
    count = dividers_count()
    while n < MAX_SIZE:
        triangle = (n * (n+1)) / 2
        #print n, count[n]
        if n%2 == 0:
            if count[n/2] * count[n+1] > 500:
                return n, triangle
        else:
            if count[n] * count[(n+1)/2] > 500:
                return n, triangle
        n += 1

if __name__ == "__main__":
    print first_triangle_number_with_over_500_dividers()
