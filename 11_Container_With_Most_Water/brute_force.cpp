class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_capacity = 0;
        int capacity;
        
        for (int i = 0; i < height.size(); i++){
            for (int j = i + 1; j < height.size(); j++){
                if (height[i] < height[j]){
                    capacity = height[i] * (j - i);
                }else{
                    capacity = height[j] * (j - i);
                }
                if (capacity > max_capacity){
                    max_capacity = capacity;
                }
            }
        }
        return max_capacity;
    }
};


// Time Complexity: O(n^2)
// Runtime: Time Limit Exceeded