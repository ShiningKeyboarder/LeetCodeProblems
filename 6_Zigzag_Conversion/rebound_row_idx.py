class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows_str = ['' for i in range(numRows)]
        row_idx = 0
        
        for c in s:
            rows_str[row_idx] += c
            if row_idx == 0:
                rebound = 1
            elif row_idx == (numRows - 1):
                rebound = -1
            row_idx += rebound
        
        ans = ''
        for row in rows_str:
            ans += row
            
        return ans

# Time Complexity: O(n)
# Runtime: 101 ms	Memory: 14.1 MB