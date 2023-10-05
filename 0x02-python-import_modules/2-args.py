#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    print("{}".format(len(sys.argv) - 1), end=" ")
    if len(sys.argv) != 2:
        print("arguments", end="")
    if len(sys.argv) == 2:
        print("argument", end="")
    if len(sys.argv) == 1:
        print(".", end="\n")
    if len(sys.argv) > 1:
        print(":", end="\n")
    if len(sys.argv) > 1:
        for x in range(1, len(sys.argv)):
            print("{}: {}".format(x, sys.argv[x]))
