class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        pairs = []
        ans = ''
        i = 0
        j = 0
        rebound = False
        for c in s:
            pairs.append((c, (i, j)))
            
            if not rebound:
                if (i + 1) == numRows:
                    rebound = True
                    i -= 1
                    j += 1
                else:
                    i += 1
            else:
                if i == 0:
                    rebound = False
                    i += 1
                else:
                    i -= 1
                    j += 1
                
            
        pairs.sort(key=lambda x: x[1])
        for pair in pairs:
            ans += pair[0]
            
        return ans


# Time Complexity: O(nlog(n))
# Runtime: 125 ms	Memory: 14.2 MB