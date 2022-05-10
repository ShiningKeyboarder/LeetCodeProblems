class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        s = str(abs(x))
        ans = sign * int(s[::-1])
        if ans < -2**31 or ans >= 2**31:
            return 0   
        return ans


# Time Complexity: O(d) = O(log(n)),  
# d: digit of the input number   
# n: value of the input number
# Runtime: 35 ms	Memory: 13.9 MB