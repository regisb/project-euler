def trailing_digits(n):
    billion = 10**9
    x = 0
    nx_last_digits = 1
    while True:
        if nx_last_digits == x:
            return x
        nx_last_digits = (nx_last_digits*n % billion)
        x += 1

if __name__ == "__main__":
    print trailing_digits(4)


