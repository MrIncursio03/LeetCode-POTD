"""

Author : Shuvam Kumar Singh
Date : 31/01/2024
Problem : 2966. Divide Array Into Arrays With Max Difference
Difficulty : Medium

"""


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n=len(nums)
        nums.sort()

        ans=[]
        for i in range(0,n,3):
            if nums[i+2]-nums[i]<=k:
                ans.append(nums[i:i+3])
            else:
                return []
        return ans
