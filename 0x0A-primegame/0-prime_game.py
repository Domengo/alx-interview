#!/usr/bin/python3
"""_summary_ - find the most wins
"""


def isWinner(x, nums):
    """_summary_ - find the most wins
    Args:
        x ([type]): [description]
        nums ([type]): [description]
    """
    if not nums or x < 1:
        return None
    n = max(nums)
    nums.sort()
    m = [False for i in range(n + 1)]
    for i in range(2, n + 1):
        if not m[i]:
            for j in range(i, n + 1, i):
                m[j] = True
    m[0] = m[1] = False
    c = 0
    for i in range(len(m)):
        if m[i]:
            c += 1
        m[i] = c
    p1 = 0
    for n in nums:
        p1 += m[n] % 2 == 1
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"
