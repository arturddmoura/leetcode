#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s, t = [*s], [*t]
        s.sort()
        t.sort()

        return t == s
# @lc code=end


solution = Solution()
print(solution.isAnagram(s="anagram", t="nagaram"))
print(solution.isAnagram(s="rat", t="car"))
print(solution.isAnagram(s="oto", t="oto"))
