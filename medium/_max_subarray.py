# Given an integer array nums, find the subarray
# with the largest sum, and return its sum.

# Kadane's Algorithm
# The most crucial observation:
# The core observation is that the maximum sum subarray ending at index i is either:
# 1. The element at index i itself, or
# 2. The maximum sum subarray ending at index i-1 extended to include the element at index i.

# In other words, at each point in the array, you have two choices: either you include
# the current element in the existing subarray sum (max_current + array[i]), or you start
# a new subarray (array[i]).

# Why It Covers All Combinations?
# Why you don't miss any possible subarray combinations even though you only go through the
# array once. The reason is that the variable max_global keeps track of the highest sum found
# so far, and max_current essentially examines all possible ending points for subarrays.

# For every index, you've considered:
# 1. All subarrays ending at that index
# 2. Whether the maximum sum subarray up to that point should be extended or reset


from typing import List

class MaxSubArray:
    def max_sub_array(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        global_max = nums[0]
        current_max = nums[0]
        for value in nums[1:]:
            current_max = value if value > value + current_max else value + current_max
            if current_max > global_max:
                global_max = current_max
        return global_max

nums = [5, 4, -1, 7, 8]
nums1 = [-2, 1,-3, 4, -1, 2, 1, -5, 4]
msa = MaxSubArray()
res = msa.max_sub_array(nums)
print(res)

