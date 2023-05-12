#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    number_elements = len(sys.argv)
    if number_elements <= 1:
        print("0 arguments.")
    else:
        if number_elements == 2:
            print("{:d} argument:".format(number_elements - 1))
        else:
            print("{:d} arguments:".format(number_elements - 1))
        for i in range(1, number_elements):
            print("{:d}: {}".format(i, sys.argv[i]))
