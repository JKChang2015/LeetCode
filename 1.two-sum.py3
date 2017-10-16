#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum
#
# algorithms
# Easy (35.09%)
# Total Accepted:    622.9K
# Total Submissions: 1.8M
# Testcase Example:  '[3,2,4]6'# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index, value in enumerate(nums):
            hash_map[value] = index
        for index1, value in enumerate(nums):
            if target - value in hash_map:
                index2 = hash_map[target - value]
                if index1 != index2:
                    return [index1, index2] 
