"""
1. Two Sum
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, value in enumerate(nums):
            left = target - value 
            find_left = hash_map.get(left, -1)
            hash_map[value] = index
            if find_left >= 0:
                return [index, find_left]
        return []