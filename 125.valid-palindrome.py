#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return_string = ""
        for char in s:
            if char.isalpha() or char.isnumeric():
                return_string += char.lower()
        return return_string == return_string[::-1]
# @lc code=end


solution = Solution()
result = solution.isPalindrome(s="A man, a plan, a canal: Panama")
print(result)
result = solution.isPalindrome(s="race a car")
print(result)
result = solution.isPalindrome(s=" ")
print(result)
