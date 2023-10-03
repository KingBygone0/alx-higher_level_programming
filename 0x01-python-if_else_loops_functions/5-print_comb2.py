#!/usr/bin/python3
for numbers in range(0, 100):
    print(f'{numbers:02}', end=', ' if numbers < 99 else '\n')
