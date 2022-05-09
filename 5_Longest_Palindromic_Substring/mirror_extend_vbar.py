class Solution: 
    def longestPalindrome(self, s: str) -> str:
        s_bar = '|' 
        for i in range(len(s)):
            s_bar += s[i] + '|'
        # i.e. if s = 'abbe'
        #      -> s_bar = '|a|b|b|e|'

        max_len = 0
        
        # Find palindrome with odd length of string
        for i in range(len(s_bar)):
            radius = 0
            while i - radius >= 0 and i + radius < len(s_bar):
                if s_bar[i - radius] == s_bar[i + radius]:
                    count = 2 * radius + 1
                    if count > max_len:
                        max_len = count
                        center = i
                    radius += 1
                else:
                    break
            
        max_radius = (max_len - 1) // 2
        ans = s_bar[(center - max_radius):(center + max_radius + 1)].replace('|', '')    
        return ans


# Time Complexity: O(n^2)
# Worst case analysis and assume n is even
# T(n) = 1 + 2 + ... + n + n+1 + n + ... + 2 + 1
#      = ((n+1) * (1 + n+1) / 2) * 2 - (n+1)
#      = (n^2 + 3n + 2) / 2 * 2 - (n+1)
#      = n^2 + 2n + 1
# Runtime: 3132 ms	Memory: 14.1 MB