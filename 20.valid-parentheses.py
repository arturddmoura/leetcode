#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'{': '}', '[': ']', '(': ')'}

        stack = []
        for char in s:
            if char in brackets:
                stack.append(char)
            elif not stack or brackets[stack.pop()] != char:
                return False
        
        return not stack
    
# @lc code=end

solution = Solution()
result = solution.isValid(s="()]{}")

print(result)
