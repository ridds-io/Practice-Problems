'''
Given the first 2 terms a and b of a Geometric Series. The task is to find the nth term of the series.

Constraints:
-100 ≤ a, b ≤ 100
1 ≤ n ≤ 9
'''

class Solution:
    def termOfGP(self, a, b, n):
        r = b / a
        return a * (r**(n-1))
