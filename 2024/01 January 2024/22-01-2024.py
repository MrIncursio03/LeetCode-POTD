"""

Author : Shuvam Kumar Singh
Date : 21/01/2024
Problem : 645. Set Mismatch
Difficulty : Easy

"""


class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    for num in nums:
      if nums[abs(num) - 1] < 0:
        duplicate = abs(num)
      else:
        nums[abs(num) - 1] *= -1

    for i, num in enumerate(nums):
      if num > 0:
        return [duplicate, i + 1]
