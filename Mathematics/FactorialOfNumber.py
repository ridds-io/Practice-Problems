'''
Given a positive integer n. You have to find factorial of n.

Constraints:
0 ≤ n ≤ 11
'''

class Solution:
    def factorial(self,n):
        if n < 0:
            return -1
        if n == 1 or n == 0:
            return 1
        return n * self.factorial(n-1)
