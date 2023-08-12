# Given an array nums of n integers, return an array of all
# the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
class FourSum(object):
    def four_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < len(nums) and nums[left] == nums[left - 1]:
                            left += 1
                    elif current_sum < target:
                        left += 1
                        # while left < len(nums) and nums[left] == nums[left - 1]:
                        #     left += 1
                    else:
                        right -= 1
                        # while right > 0 and nums[right] == nums[right + 1]:
                        #     right -= 1

        return result


print(FourSum().four_sum([-2, -1, -1, 1, 1, 2, 2], 0))
