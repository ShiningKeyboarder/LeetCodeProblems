class Solution {
public:
    string longestPalindrome(string s) {
        int n = s.size();
        string s_bar = "|";
        for (int i = 0; i < n; i++){
            s_bar += s[i];
            s_bar += '|';
        }
        // i.e. if s = 'abbe'
        //      -> s_bar = '|a|b|b|e|'

        int center = 0;
        int radius = 0;
        int old_center, old_radius;
        int border_radius, mirrored_center;
        int m = s_bar.size();
        int palindrome_radius[m];

        while (center < m){
            while ((center - (radius + 1)) >= 0 && (center + (radius + 1)) < m){
                if (s_bar[center - (radius + 1)] == s_bar[center + (radius + 1)])
                    radius++;
                else break;
            }
            palindrome_radius[center] = radius;
            
            old_center = center;
            old_radius = radius;

            center++;
            radius = 0;

            while (center <= old_center + old_radius){
                border_radius = old_center + old_radius - center;
                mirrored_center = old_center - (center - old_center);

                if (palindrome_radius[mirrored_center] < border_radius){
                    palindrome_radius[center] = palindrome_radius[mirrored_center];
                }
                else if(palindrome_radius[mirrored_center] > border_radius){
                    palindrome_radius[center] = border_radius;
                }
                else{
                    radius = border_radius;
                    break;
                }
                center++;
            }
        }

        int max_radius = 0;
        int best_center, r_center, r_radius;
        string ans = "";
        for (int i = 0; i < m; i++){
            if (palindrome_radius[i] > max_radius){
                max_radius = palindrome_radius[i];
                best_center = i;
            }
        }
        
        if (s_bar[best_center] == '|'){
            r_center = best_center / 2;
            r_radius = max_radius / 2;
            ans = s.substr(r_center - r_radius, 2 * r_radius);
        }else{
            r_center = (best_center - 1) / 2;
            r_radius = (max_radius - 1) / 2;
            ans = s.substr(r_center - r_radius, 2 * r_radius + 1);
        }
        return ans;
    }
};


// Time Complexity: O(n)
// Runtime: 7 ms	Memory: 7.9 MB