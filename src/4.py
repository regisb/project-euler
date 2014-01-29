#! /usr/bin/env python

def is_palindrome(number):
    string = str(number)
    string_length = len(string)
    for index in range(0, string_length/2):
        if string[index] != string[string_length - 1 - index]:
            return False
    return True

def find_largest_palindrome():
    largest_palindrome = -1
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i*j
            if is_palindrome(product):
                if largest_palindrome < 0 or product > largest_palindrome:
                    largest_palindrome = product
    return largest_palindrome

if __name__ == "__main__":
    print find_largest_palindrome()
