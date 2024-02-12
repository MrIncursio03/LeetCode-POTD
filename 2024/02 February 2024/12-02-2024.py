"""

Author : Shuvam Kumar Singh
Date : 12/02/2024
Problem : 169. Majority Element
Difficulty : Easy

"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        n = len(nums) // 2

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            if count > n:
                return num

