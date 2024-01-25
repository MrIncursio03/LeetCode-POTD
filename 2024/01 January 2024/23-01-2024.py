"""

Author : Shuvam Kumar Singh
Date : 23/01/2024
Problem : 1239. Maximum Length of a Concatenated String with Unique Characters
Difficulty : Medium

"""


class Solution:
    def maxLength(self, arr):
        masks = []

        for s in arr:
            mask = self.get_mask(s)
            if mask != -1:
                masks.append(mask)

        return self.dfs(masks, 0, 0)

    def dfs(self, masks, s, used):
        res = bin(used).count('1')
        for i in range(s, len(masks)):
            if (used & masks[i]) == 0:
                res = max(res, self.dfs(masks, i + 1, used | masks[i]))
        return res

    def get_mask(self, s):
        mask = 0
        for c in s:
            i = ord(c) - ord('a')
            if (mask & (1 << i)) != 0:
                return -1
            mask |= 1 << i
        return mask


# Example usage:
arr = ["un", "iq", "ue"]
sol = Solution()
result = sol.maxLength(arr)
print(result)
