class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int remainder;
        vector<int> indices;
        unordered_map<int, int> umap;
        for (int i = 0; i < nums.size(); i++){
            remainder = target - nums[i];
            if (umap.count(remainder)){
                indices.push_back(i);
                indices.push_back(umap[remainder]);
                return indices;
            }
            umap[nums[i]] = i;
        }
        return indices;
    }
};

// Time Complexity: O(n)
// Runtime: 8 ms	Memory: 10.8 MB