class Solution {
public:
    string longestPalindrome(string s) {
        string ans = "";
        int max_len = 0;
        int n = s.size();

        // Find palindrome with odd length of string
        for (int i = 0; i < n; i++){
            int radius = 0;
            while ((i - radius) >= 0 && (i + radius) < n){
                if (s[i - radius] == s[i + radius]){
                    if ((2 * radius + 1) > max_len){
                        max_len = 2 * radius + 1;
                        ans = s.substr(i - radius, max_len);
                    }
                    radius++;
                }
                else break;
            }
        }

        // Find palindrome with even length of string
        for (int i = 0; i < n-1; i++){
            int radius = 0;
            while ((i - radius) >= 0 && (i + 1 + radius) < n){
                if (s[i - radius] == s[i + 1 + radius]){
                    if ((2 * radius + 2) > max_len){
                        max_len = 2 * radius + 2;
                        ans = s.substr(i - radius, max_len);
                    }
                    radius++;
                }
                else break;
            }
        }
        
        return ans;
    }
};


// Time Complexity: O(n^2)
// Worst case analysis and assume n is even
// T(n) = (1 + 2 + ... + (n/2-1) + (n/2) + (n/2) + (n/2-1) + ... + 2 + 1) 
//        + (1 + 2 + ... + (n/2-1) + (n/2) + (n/2-1) + ... + 2 + 1)
//      = (n/2 * (1 + n/2) / 2) * 4 - n/2
//      = (n^2 + n) / 2
// Runtime: 69 ms	Memory: 21.2 MB