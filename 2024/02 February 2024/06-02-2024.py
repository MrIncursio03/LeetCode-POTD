"""

Author : Shuvam Kumar Singh
Date : 06/02/2024
Problem : 49. Group Anagrams
Difficulty : Easy

"""


class Solution:
    def groupAnagrams(self, strs):
        dic = collections.defaultdict(list)
        for s in strs: 
            dic["".join(sorted(s))].append(s)
        return list(dic.values())
