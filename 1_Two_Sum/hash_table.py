class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num2idx = {}
        for i in range(len(nums)):
            value = hash_num2idx.get(target-nums[i])
            if value != None:
                return i, value
            hash_num2idx[nums[i]] = i

# Time Complexity: O(n)
# Runtime: 122 ms	Memory: 15.2 MB