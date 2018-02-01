"""
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.
You may assume that each input would have exactly one solution, and you may
not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # corner case
        if len(nums) == 0:
            return None
        previous_dict = dict()
        return_list = []
        for index, num in enumerate(nums):
            if num in previous_dict:
                return_list = [previous_dict[num], index]
            previous_dict[target - num] = index
        if len(return_list) == 0:
            return None
        else:
            return return_list
