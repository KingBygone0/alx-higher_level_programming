#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    sym = [43, 45, 42, 47]
    cont = 0

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    for x in sym:
        if x == ord(sys.argv[2]):
            cont = cont + 1

    if cont == 0:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if ord(sys.argv[2]) == 43:
        resul = add(int(sys.argv[1]), int(sys.argv[3]))

    if ord(sys.argv[2]) == 45:
        resul = sub(int(sys.argv[1]), int(sys.argv[3]))

    if ord(sys.argv[2]) == 42:
        resul = mul(int(sys.argv[1]), int(sys.argv[3]))

    if ord(sys.argv[2]) == 47:
        resul = div(int(sys.argv[1]), int(sys.argv[3]))

    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], resul))
