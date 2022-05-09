class Solution: 
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ans = ''
        
        # Find palindrome with odd length of string
        for i in range(len(s)):
            radius = 0
            while i - radius >= 0 and i + radius < len(s):
                if s[i - radius] == s[i + radius]:
                    count = 2 * radius + 1
                    if count > max_len:
                        max_len = count
                        ans = s[(i - radius):(i + radius + 1)]
                    radius += 1
                else:
                    break
        
        # Find palindrome with even length of string
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                radius = 0
                while i - radius >= 0 and i + 1 + radius < len(s):
                    if s[i - radius] == s[i + 1 + radius]:
                        count = 2 * radius + 2
                        if count > max_len:
                            max_len = count
                            ans = s[(i - radius):(i + radius + 2)]
                        radius += 1
                    else:
                        break
                        
        return ans


# Time Complexity: O(n^2)
# Worst case analysis and assume n is even
# T(n) = (1 + 2 + ... + (n/2-1) + (n/2) + (n/2) + (n/2-1) + ... + 2 + 1) 
#        + (1 + 2 + ... + (n/2-1) + (n/2) + (n/2-1) + ... + 2 + 1)
#      = (n/2 * (1 + n/2) / 2) * 4 - n/2
#      = (n^2 + n) / 2
# Runtime: 1638 ms	Memory: 13.9 MB