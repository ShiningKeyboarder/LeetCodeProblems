import numpy as np


class Solution: 
    def longestPalindrome(self, s: str) -> str:
        # Manacher's Algorithm  Time:O(n)
        s_bar = '|' 
        for i in range(len(s)):
            s_bar += s[i] + '|'
        # i.e. if s = 'abbe'
        #      -> s_bar = '|a|b|b|e|'
        
        palindrome_radius = np.zeros(len(s_bar), dtype='int32')
        center = 0
        radius = 0
        
        while center < len(s_bar):
            while center - (radius + 1) >= 0 and center + (radius + 1) < len(s_bar):
                if s_bar[center - (radius + 1)] == s_bar[center + (radius + 1)]:
                    radius += 1
                else:
                    break
            
            palindrome_radius[center] = radius
            
            old_center = center
            old_radius = radius
            
            center += 1
            radius = 0
            
            while center <= old_center + old_radius:
                border_radius = old_center + old_radius - center
                mirriored_center = old_center - (center - old_center)
                
                if palindrome_radius[mirriored_center] < border_radius:
                    palindrome_radius[center] = palindrome_radius[mirriored_center]
                elif palindrome_radius[mirriored_center] > border_radius:
                    palindrome_radius[center] = border_radius
                else:
                    radius = border_radius
                    break    
                center += 1
                
                    
        best_center = np.argmax(palindrome_radius)
        max_radius = palindrome_radius[best_center]
        ans = s_bar[(best_center - max_radius):(best_center + max_radius + 1)].replace('|', '')    
        return ans


# Time Complexity: O(n)
# Runtime: 940 ms	Memory: 32 MB