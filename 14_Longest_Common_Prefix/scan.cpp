class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int min_len = INT_MAX;
        string ans = "";
        char c;
        
        for (int i = 0; i < strs.size(); i++){
            if (strs[i].length() < min_len){
                min_len = strs[i].length();
            }
        }
        
        for (int i = 0; i < min_len; i++){
            c = strs[0][i];
            for (int j = 1; j < strs.size(); j++){
                if (strs[j][i] != c){
                    return ans;
                }
            }
            ans += c;
        }
        
        return ans;
    }
};


// Time Complexity: O(SN)
// S: The length of the shortest string
// N: The number of strings
// Runtime: 8 ms	Memory: 9.2 MB