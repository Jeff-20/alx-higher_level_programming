#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    name = dir(hidden_4)
    for i in range(0, len(name)):
        if "__" not in name[i]:
            print(name[i])
