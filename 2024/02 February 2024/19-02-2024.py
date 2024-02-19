"""

Author : Shuvam Kumar Singh
Date : 19/02/2024
Problem : 231. Power of Two
Difficulty : Easy

"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==0:
            return False
        while n%2==0:
            n=n/2
        return n==1
