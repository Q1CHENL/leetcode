# From leetcode, even 3x faster than 2 ptr method
from collections import *

class ThreeSum:
    def threeSum(self, nums):
        triplets = []
        d = Counter(nums) # remove duplicates, and Counter is a dict, which makes lookup so fast
        for num, count in d.items():
            if count < 2:
                continue
            target = -2 * num
            if target not in d:
                continue
            if target == 0 and count < 3:
                continue
            triplets.append([target, num, num])
        keys = sorted(d.keys())
        for i, a in enumerate(keys):
            if a >= 0:
                break
            for b in keys[i + 1:]:
                c = -a - b
                if c <= b:
                    break
                if c not in d: # lookup in Counter dict, O(1) time, main reason why this method fast
                    continue
                triplets.append([a, b, c])
        return triplets
        # l = bisect.bisect_left(keys, -(a + keys[-1]), i + 1)
        # r = bisect.bisect_left(keys, -(a / 2), l)

    # class ThreeSum:
    # From ChatGPT: 2 ptrs method
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
