#!/usr/bin/python3
"""
Define isWineer function, a solution to the Prime Game problem
"""


def primes(n):
    """Return list of prime numbers between 1 and n inclusive
        Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
    Args:
        x (int): no. of rounds of game
        nums (int): upper limit of range for each round
    Return:
        Name of winner (Maria or Ben) or None if winner cannot be found
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = primes(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
# def isWinner(x, nums):
#     """_summary_ - find the most wins
#     Args:
#         x ([type]): [description]
#         nums ([type]): [description]
#     """
#     if not nums or x < 1:
#         return None
#     n = max(nums)
#     nums.sort()
#     m = [False for i in range(n + 1)]
#     for i in range(2, n + 1):
#         if not m[i]:
#             for j in range(i, n + 1, i):
#                 m[j] = True
#     m[0] = m[1] = False
#     c = 0
#     for i in range(len(m)):
#         if m[i]:
#             c += 1
#         m[i] = c
#     p1 = 0
#     for n in nums:
#         p1 += m[n] % 2 == 1
#     if p1 * 2 == len(nums):
#         return None
#     if p1 * 2 > len(nums):
#         return "Maria"
#     return "Ben"
