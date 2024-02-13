"""

Author : Shuvam Kumar Singh
Date : 13/02/2024
Problem : 2108. Find First Palindromic String in the Array
Difficulty : Easy

"""


class Solution(object):
    def firstPalindrome(self, words):
        for word in words:
            if word == word[::-1]:
                return word
        return ""
