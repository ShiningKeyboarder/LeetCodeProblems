class Solution {
public:
    bool check_palindromic(string s){
        int n = s.size();
        for (int i = 0; i < n; i++){
            if (s[i] != s[n-1-i])
                return false;
        }
        return true;
    }

    string longestPalindrome(string s) {
        string ans = "";
        int max_len = 0;
        int n = s.size();

        for (int i = 0; i < n; i++){
            for (int len = 1; len <= n-i; len++){
                if (check_palindromic(s.substr(i, len)) && s.substr(i, len).size() > max_len){
                    max_len = s.substr(i, len).size();
                    ans = s.substr(i, len);
                }
            }
        }
        return ans;
    }
};


// Time Complexity: O(n^3)
// Runtime: Time Limit Exceeded