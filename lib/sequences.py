#!/usr/bin/env python3


def print_fibonacci(length):
    a, b = 0, 1
    result = []
    for _ in range(length):
        result.append(a)
        a, b = b, a + b
    print(result)
