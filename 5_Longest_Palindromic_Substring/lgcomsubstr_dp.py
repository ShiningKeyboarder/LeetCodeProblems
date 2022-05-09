import numpy as np

class Solution: 
    def longestPalindrome(self, s: str) -> str:
        s_rev = s[::-1]
        return self.longestCommonSubstr(s, s_rev)
        
    def longestCommonSubstr(self, s1: str, s2: str) -> str:
        L = np.zeros((len(s1)+1, (len(s2))+1), dtype=int)
        max_len = 0
        ans = ''
        
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    L[i, j] = L[i-1, j-1] + 1
                    if L[i, j] > max_len and (i - L[i, j] + j) == len(s1):
                        max_len = L[i, j]
                        ans = s1[(i - L[i, j]):i]
        return ans

# Time Complexity: O(n^2)
# Runtime: Time Limit Exceeded