class Solution:
    def intToRoman(self, num: int) -> str:
        sym_list = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        val_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ''
        for i in range(13):
            count = num // val_list[i]
            num = num % val_list[i]
            for j in range(count):
                ans += sym_list[i]
        return ans


# Time Complexity: O(1)
# Runtime: 66 ms	Memory: 13.9 MB