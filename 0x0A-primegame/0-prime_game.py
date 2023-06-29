#!/usr/bin/python3
"""_summary_ - find the most wins
"""


def isWinner(x, nums):
    """_summary_

    Args:
        x (_type_): _description_
        nums (_type_): _description_

    Returns:
        _type_: _description_
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = [True] * (n+1)
        primes[0] = primes[1] = False

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False

        # Determine the winner for the current round
        if primes.count(True) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
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
