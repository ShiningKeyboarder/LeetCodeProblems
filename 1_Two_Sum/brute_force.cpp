class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int a, b;
        vector<int> indices;
        for (int i = 0; i < nums.size()-1; i++){
            a = nums[i];
            for (int j = i+1; j < nums.size(); j++){
                b = nums[j];
                if (a + b == target){
                    indices.push_back(i);
                    indices.push_back(j);
                    return indices;
                }
            }
        }
        return indices;
    }
};

// Time Complexity: O(n^2)
// Runtime: 410 ms	Memory: 10.2 MB