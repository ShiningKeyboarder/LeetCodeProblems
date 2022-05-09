class Solution: 
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        ans = ''
        
        s_rev = s[::-1]
        start1 = 0
        start2 = len(s_rev) - 1
        
        for slide in range(len(s)+len(s_rev)-1):
            i = start1
            j = start2
            c_len = 0
            substr_head = start1
            while i < len(s) and j <len(s_rev):
                if s[i] == s_rev[j]:
                    c_len += 1
                    if c_len > max_len and substr_head == (len(s)-j-1):
                        max_len = c_len
                        ans = s[substr_head:i+1]
                else:
                    c_len = 0
                    substr_head = i + 1
     
                i += 1
                j += 1
                
            if start2 > 0:
                start2 -= 1
            else:
                start1 += 1
      
        return ans


# Time Complexity: O(n^2)
# T(n) = 1 + 2 + ... + n-1 + n + n-1 + ... + 2 + 1
#      = (n * (1 + n) / 2) * 2 - n
#      = n^2
# Runtime: Time Limit Exceeded