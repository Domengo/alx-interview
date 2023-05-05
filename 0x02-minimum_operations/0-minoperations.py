#!/usr/bin/python3
"""return an integer"""


def minOperations(n):
    ''''minimum operations'''
    if n == 1:
        return 0

    operations = 0
    h_count = 1
    clipboard = 1

    while h_count < n:
        if n % h_count == 0:
            clipboard = h_count
        h_count += clipboard
        operations += 1

    if h_count == n:
        return operations
    else:
        return 0
# def minOperations(n):
#     
#     if n < 2:
#         return 0

#     count = 0
#     op = 2

#     while n > 1:
#         if not n % op:
#             n //= op
#             count += op

#         else:
#             if op == 2:
#                 op += 1
#             else:
#                 op += 2

#     return count
