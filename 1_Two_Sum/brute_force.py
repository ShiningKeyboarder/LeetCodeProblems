class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            a = nums[i]
            for j in range(i+1, n):
                b = nums[j]
                if a + b == target:
                    return i, j

# Time Complexity: O(n^2)
# Runtime: 4861 ms	Memory: 15 MB