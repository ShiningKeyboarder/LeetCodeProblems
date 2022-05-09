class Solution:
    def check_palindromic(self, s:str) -> bool:
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n-i-1]:
                return False
        return True
    
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if self.check_palindromic(s[i:j]) and len(s[i:j]) > max_len:
                    max_len = len(s[i:j])
                    ans = s[i:j]
        
        return ans

# Time Complexity: O(n^3)
# Runtime: Time Limit Exceeded