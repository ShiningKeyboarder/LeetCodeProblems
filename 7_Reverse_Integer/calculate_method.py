class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        x_rev = 0
        
        while x != 0:
            digit = x % 10
            x = x // 10
            x_rev = x_rev * 10 + digit
            
        x_rev = sign * x_rev
        if x_rev < -2**31 or x_rev >= 2**31:
            return 0   
        return x_rev

# Time Complexity: O(d) = O(log(n)),  
# d: digit of the input number   
# n: value of the input number
# Runtime: 45 ms	Memory: 13.9 MB