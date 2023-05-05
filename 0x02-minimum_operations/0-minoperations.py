#!/usr/bin/python3
"""return an integer"""


def minOperations(n):
    '''minimum operations'''
    if n < 2:
        return 0

    count = 0
    op = 2

    while n > 1:
        if not n % op:
            n //= op
            count += op

        else:
            if op == 2:
                op += 1
            else:
                op += 2

    return count
