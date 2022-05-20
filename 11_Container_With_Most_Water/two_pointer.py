class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = 0
        i = 0
        j = len(height) - 1
        
        for _ in range(len(height) - 1):
            if height[i] < height[j]:
                capacity = height[i] * (j - i)
                i += 1
            else:
                capacity = height[j] * (j - i)
                j -= 1
                
            if capacity > max_capacity:
                max_capacity = capacity
                
        return max_capacity


# Time Complexity: O(n)
# Runtime: 782 ms	Memory: 27.5 MB