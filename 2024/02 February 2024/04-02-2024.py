"""

Author : Shuvam Kumar Singh
Date : 04/02/2024
Problem : 76. Minimum Window Substring
Difficulty : Hard

"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        char_count = [0] * 128  # Use an array to store character counts
        count = len(t)
        start = 0
        end = 0
        min_len = float('inf')
        start_index = 0

        # Initialize char_count array with character counts from string t
        for char in t:
            char_count[ord(char)] += 1

        while end < len(s):
            if char_count[ord(s[end])] > 0:
                count -= 1
            char_count[ord(s[end])] -= 1
            end += 1

            while count == 0:
                if end - start < min_len:
                    start_index = start
                    min_len = end - start

                if char_count[ord(s[start])] == 0:
                    count += 1
                char_count[ord(s[start])] += 1
                start += 1

        return "" if min_len == float('inf') else s[start_index:start_index + min_len]
