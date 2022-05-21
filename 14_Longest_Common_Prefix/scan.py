class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(strs[i]) for i in range(len(strs))])
        ans = ''
        
        for i in range(min_len):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return ans
            ans += c
        
        return ans


# Time Complexity: O(SN)
# S: The length of the shortest string
# N: The number of strings
# Runtime: 56 ms	Memory: 13.9 MB