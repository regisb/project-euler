def digit_canceling_fractions():
    for x in range(1, 10):
        for y in range(1, 10):
            for z in range(1, 10):
                xy = int(str(x) + str(y))
                yx = int(str(y) + str(x))
                yz = int(str(y) + str(z))
                zy = int(str(z) + str(y))
                if xy < yz and 9*x*z + y*z - 10*x*y == 0:
                    print "1)", str(x) + str(y) + "/" + str(y) + str(z)
                if yx < zy and 10*y*z - x*y - 9*x*z == 0:
                    print "2)", str(y) + str(x) + "/" + str(z) + str(y)

if __name__ == "__main__":
    digit_canceling_fractions()
