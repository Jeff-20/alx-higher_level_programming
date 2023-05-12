#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    number_elements = len(argv)
    total_num = 0

    for i in range(1, number_elements):
        total_num += int(argv[i])
    print("{:d}".format(total_num))
