class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows_str = ['' for i in range(numRows)]
        mod = (numRows - 1) * 2
        
        for i in range(len(s)):
            pos = i % mod
            if pos >= numRows:
                pos = mod - pos
            rows_str[pos] += s[i]
        
        ans = ''
        for row in rows_str:
            ans += row
            
        return ans

# Time Complexity: O(n)
# Runtime: 88 ms	Memory: 14 MB