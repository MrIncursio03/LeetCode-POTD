"""

Author : Shuvam Kumar Singh
Date : 02/02/2024
Problem : 1291. Sequential Digits
Difficulty : Medium

"""

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        t = '123456789'
        l = []
        for i in range(len(t)):
            for j in range(i+1, len(t)+1):
                if low <= int(t[i:j]) <= high:
                    l.append(int(t[i:j]))
        return sorted(l)
        
