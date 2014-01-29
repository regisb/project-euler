import euler
from math import sqrt

if __name__ == "__main__":
    text = open("words.txt").read()
    words = text.replace("\"", "").split(",")
    count = 0
    for word in words:
        word_value = euler.string_value(word)
        n = int(sqrt(2*word_value))
        if n*(n+1) == 2*word_value:
            print word_value
            count += 1
    print count
