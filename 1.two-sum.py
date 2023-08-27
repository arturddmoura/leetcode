#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            difference = target - num
            if difference in hashmap:
                return [index, hashmap[difference]]
            hashmap[num] = index
                         
# @lc code=end

solution = Solution()
print(solution.twoSum([3,2,4], 6))