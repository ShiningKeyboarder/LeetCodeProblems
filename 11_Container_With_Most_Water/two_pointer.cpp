class Solution {
public:
    int maxArea(vector<int>& height) {
        int max_capacity = 0;
        int capacity;
        int i = 0;
        int j = height.size() - 1;
        
        while (i != j){
            if (height[i] < height[j]){
                capacity = height[i] * (j - i);
                i++;
            }else{
                capacity = height[j] * (j - i);
                j--;
            }
            if (capacity > max_capacity){
                max_capacity = capacity;
            }

        }
        return max_capacity;
    }
};


// Time Complexity: O(n)
// Runtime: 99 ms	Memory: 59 MB