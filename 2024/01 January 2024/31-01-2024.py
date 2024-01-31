"""

Author : Shuvam Kumar Singh
Date : 31/01/2024
Problem : 739. Daily Temperatures
Difficulty : Medium

"""


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index

            stack.append(i)

        return ans
