#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    a = 0
    for i in range(1, len(argv)):
        a += int(argv[i])
        i += 1
    print(f"{a}")
