#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        for i in range(1, len(argv)):
            print("1 argument:")
            print("{}: {}".format(i, argv[i]))
    else:
        i = 2
        print("{} arguments:".format((len(argv) - 1)))
        print("{}: {}".format((i - 1), argv[i - 1]))
        while i < len(argv):
            print("{}: {}".format((i), argv[i]))
            i += 1
