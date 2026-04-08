'''
Given an integer n, find the number of digits in the value of n factorial. 

Examples :

Input: n = 5
Output: 3
Explanation: Factorial of 5 is 120. Number of digits in 120 is 3 (1, 2, and 0)

Input: n = 120
Output: 199
Explanation: The number of digits in 120! is 199

Constraints:
1 ≤ n ≤ 105

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)
'''

import math

class Solution:
    def digitsInFactorial(self,n):
        if n < 0:
            return 0
        if n == 0 or n == 1:
            return 1
        x = (n * math.log10(n / math.e) + (math.log10(2 * math.pi * n) / 2.0))
        return math.floor(x) + 1
            
'''
KAMENETSKY'S FORMULA:

x = (n * math.log10(n / math.e) + (math.log10(2 * math.pi * n) / 2.0))
return math.floor(x) + 1

'''

# Possible Solution Brainstorming

'''
Estimation by Sum of Digits:

the number of digits in a product of a number with M digits and
a number with N no. of digits is usually always M + N or M + N - 1

if the leading digits of the two numbers's sum is <= 10, 
use M + N - 1

eg.> 128 * 236
     3 + 3 = 6
     1 * 2 = 2 < 10
     thus, no. of digits in 128 * 236 = 6 - 1 = 5
'''

'''
Implementation in Factorial:

1. Have to use recursion
2. Has to start from 0 and 1, like fibonacci, and go upto n
3. You will find no. of digits in product of 
i * fact(so far) {using M = no. of digits of i and N = no. of digits in fact}
at each iteration, and update that to be the new N

Loop will run from i = 1 till n ->
n < 0, will return 0
n = 0, will return 1
n > 0, will work in this function, considering initial fact value to be 0

eg.> 1 * 0! (1)
     1 + 1 = 2
     1 * 1 = 1 < 10
     thus, no. of digits in 1! = 2 - 1 = 1
     
     6 * 5! (120)
     1 + 3 = 4 
     {function will start from this step directly, 
     as only no. of digits are getting used in the function, 
     hence, avoiding calculation of factorial in cases where n is large.}
     1 * 1 = 1 < 10
     thus, no. of digits in 1! = 2 - 1 = 1

    !! HOWEVER YOU STILL NEED THE FIRST DIGIT TO DECIDE WHICH FORMULA TO USE
'''
