'''
Given a positive integer value n. The task is to find how many numbers less than or equal to n have numbers of divisors exactly 3.

Examples:

Input: n = 6
Output: 1
Explanation: The only number less than 6 with 3 divisors is 4 which has 1, 2 and 4 as divisors.

Input: n = 10
Output: 2
Explanation: 4 and 9 have 3 divisors.

Constraints : 
1 ≤ n ≤ 109

Expected Complexities

Time Complexity: O(n^(3/4))
Auxiliary Space: O(1)
'''

import math

class Solution:
    def exactly3Divisors(self,n):
        limit = int(math.sqrt(n)) # we only need prime numbers up to sqrt(n)
        
        if n < 4:
            return 0
            
        # Using Sieve of Eratosthenes
        prime = [True] * (limit + 1)
        p = 2
        while(p * p <= limit):
            if prime[p]:
                for i in range(p * p, limit + 1, p):
                    prime[i] = False
            p += 1
        
        return sum(1 for p in range(2, limit + 1) if prime[p])

'''
Exactly 3 divisors means values that are squares of prime numbers.
1, root x, and x

If  square root x is a perfect integer, then x is a square. 
'''

'''
SIEVE OF ERATOSTHENES ALGORITHM ->

1. Create a "checklist": list of (limit + 1) booleans all set to True
2. Mark Non-Primes: set 0 and 1 to False
3. Start at 2: is a Prime so leave it as True
4. Eliminate Multiples: jump through the list in steps of p, mark as False
5. Move to next True
6. Repeat until p * p > limit
7. Any number still marked True is a Prime number.
'''

# Possible Solution Brainstorming

# (functional but inefficient for large values of n)
'''
    def exactly3Divisors(self,n):
        num_count = 0
        
        if n == 1:
            return 0
            
        for i in range(2, n+1):
            root = math.sqrt(i)
            if root.is_integer() and self.isPrime(root):
                num_count += 1
        return num_count
        
    def isPrime(self, n):
        if n == 1:
            return False
            
        if n == 2 or n == 3:
            return True
                
        if n % 2 == 0 or n % 3 == 0:
            return False
                
        i = 5
            
        while (i*i <= n):
            if (n % i) == 0 or (n % (i + 2)) == 0:
                return False
                
            i += 6
                
        return True
'''    
    

