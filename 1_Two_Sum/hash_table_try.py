class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num2idx = {}
        for i in range(len(nums)):
            try:
                return i, hash_num2idx[target-nums[i]]
            except KeyError:
                pass
            hash_num2idx[nums[i]] = i

# Time Complexity: O(n)
# Runtime: 72 ms	Memory: 15.2 MB