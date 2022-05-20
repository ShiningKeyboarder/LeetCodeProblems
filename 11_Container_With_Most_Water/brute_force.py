class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_capacity = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                capacity = min(height[i], height[j]) * (j - i)
                if capacity > max_capacity:
                    max_capacity = capacity
        return max_capacity


# Time Complexity: O(n^2)
# Runtime: Time Limit Exceeded