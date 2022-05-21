class Solution {
public:
    string intToRoman(int num) {
        vector<string> sym_list = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        vector<int> val_list = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        string ans;
        int count;
        
        for (int i = 0; i < 13; i++){
            count = num / val_list[i];
            num = num % val_list[i];
            for (int j = 0; j < count; j++){
                ans += sym_list[i];
            }
        }
        return ans;
    }
};


// Time Complexity: O(1)
// Runtime: 7 ms	Memory: 8.8 MB