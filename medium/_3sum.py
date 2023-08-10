from collections import *
# Given an integer array nums, return ALL the triplets [nums[i], nums[j], nums[k]] such 
# that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# From leetcode, even 3x faster than 2 ptr method
class ThreeSum:
    def threeSum(self, nums):
        triplets = []
        # get the count of each number in nums: 
        # remove duplicates, and Counter is a dict, which makes lookup so fast
        d = Counter(nums) 
        
        # This for-loop check for triplets that could contains duplicates
        for num, count in d.items():
            # No duplicates: Such case will be handled in the loop below
            if count < 2:
                continue
            # If we found a number num that appears twice, then we need to
            # find a target = -2 * num such that the sum of those three is 0 
            target = -2 * num
            # if the target is not found
            if target not in d:
                continue
            # Or the target is 0, which means our num was also 0(== target): case [0, 0, 0]
            # which means we must have at least 3 0s in the list, otherwise we would add
            # [0, 0, 0] to the result which is wrong.
            # This ensures that we don't take one of the num == 0 as our target 
            if target == 0 and count < 3:
                continue
            # add the triplet to our final result set
            triplets.append([target, num, num])
        
        # handle unique numbers
        keys = sorted(d.keys())
        for i, a in enumerate(keys):
            # We break out of the loop if we encounter a non-negative number because
            # we're interested in numbers such that when combined with two other 
            # numbers, they sum up to zero.
            if a >= 0:
                break
            # For each unique number a, we iterate over the remaining numbers to find 
            # pairs b and c such that a + b + c = 0.
            for b in keys[i + 1:]:
                c = -a - b
                # However, if c is less than or equal to b, we break out of the loop. 
                # This is because we've already considered such combinations in the 
                # past (due to sorting), and it also helps in ensuring that the 
                # solution does not contain duplicate triplets.
                if c <= b:
                    break
                if c not in d: # lookup in Counter dict, O(1) time, main reason why this method fast
                    continue
                triplets.append([a, b, c])
        return triplets
        # l = bisect.bisect_left(keys, -(a + keys[-1]), i + 1)
        # r = bisect.bisect_left(keys, -(a / 2), l)

    # From ChatGPT: 2 ptrs method
    # class ThreeSum:
    # def three_sum(self, nums: list[int]) -> list[list[int]]:
    #     triplets = []
    #     len_nums = len(nums)
    #     nums.sort()  # sort the input list first
    #     for i in range(len_nums - 2):
    #         # skip all positive integers since nums is already sorted
    #         if nums[i] > 0:
    #             break
    #         if i > 0 and nums[i] == nums[i-1]:
    #             continue  # skip duplicates
    #         j, k = i+1, len_nums-1  # initialize two pointers
    #         while j < k:
    #             s = nums[i] + nums[j] + nums[k]
    #             if s == 0:
    #                 triplets.append([nums[i], nums[j], nums[k]])  # add tuple to set
    #                 j += 1
    #                 k -= 1
    #                 while j < k and nums[j] == nums[j-1]:
    #                     j += 1  # skip duplicates at left
    #                 while j < k and nums[k] == nums[k+1]:
    #                     k -= 1  # skip duplicates at right
    #             elif s < 0:
    #                 j += 1 # try bigger number
    #             else:
    #                 k -= 1 # try smaller number
    #     return triplets  # convert set to list of lists

    # My original idea: 3 loops, time consuming, correct but time exceeded
    # def three_sum(self, nums: list[int]) -> list[list[int]]:
    #     triplets = set()
    #     len_nums = len(nums)
    #     nums.sort()
    #     for i in range(len_nums):
    #         if nums[i] > 0:
    #             break
    #         if i > 1 and nums[i] == nums[i-1]:
    #             continue
    #         rest_1 = - nums[i]
    #         for j in range(i + 1, len_nums):
    #             rest_2 = rest_1 - nums[j]
    #             for k in range(j + 1, len_nums):
    #                 if nums[k] == rest_2:
    #                     triplets.add(
    #                         (nums[i], nums[j], nums[k])
    #                     )
    #     return [list(t) for t in triplets]
ts = ThreeSum()
nums = [-1, 0, 1, 2, -1, -4]
nums2 = [0, 0, 0]
numsorted = [-4, -1, 0, 1, 2]

lst = ts.three_sum(nums)
print(lst)
