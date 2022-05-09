class Solution:
    def binary_search(self, nums: List[int], target: int):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1
        return None

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted2orig = sorted(range(len(nums)), key=lambda k: nums[k])
        nums.sort()
        for i in range(len(nums)):
            remainder = target - nums[i]
            idx = self.binary_search(nums, remainder)
            if idx != None and idx != i:
                return sorted2orig[i], sorted2orig[idx]

# Time Complexity: O(nlog(n))
# Runtime: 103 ms	Memory: 15 MB
