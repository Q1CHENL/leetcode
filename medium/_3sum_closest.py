# Given an integer array nums of length n and an integer target, find
# three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.
from collections import *


class ThreemSumClosest(object):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    # From ChatGPT: 2-pointer approach
     def three_sum_closest(self, nums, target):
        nums.sort()
        closest = float('inf')
        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest
    
    
    # My method (Time exceeded): similar to normal 3Sum, but in this case, the distance can 
    # vary which leads to much more time of search
    # def three_sum_closest(self, nums, target):
    #     distance = 0
    #     real_targets = []
    #     dict = Counter(nums)
    #     if len(nums) == 3:
    #         return nums[0] + nums[1] + nums[2]
    #     while True:
    #         for num, count in dict.items():
    #             # num + num + (target-2 * num) = target
    #             # handle pairs
    #             if count < 2:
    #                 continue
    #             real_targets = [target - num * 2 +
    #                             distance, target - num * 2 - distance]
    #             if real_targets[0] not in dict and real_targets[1] not in dict:
    #                 continue
    #             if target == 0 and count < 3:
    #                 continue
    #             print(f'{res} {a} {b}')
    #             return (real_targets[0] if real_targets[0] in dict else real_targets[1]) + num * 2
    #         keys = sorted(dict.keys())
    #         for i, a in enumerate(keys):
    #             # if a >= target:
    #             #     break
    #             for b in keys[i+1:]:
    #                 real_targets = [target - a - b +
    #                                 distance, target - a - b - distance]
    #                 if real_targets[0] <= b and real_targets[1] <= b:
    #                     break
    #                 if real_targets[0] not in dict and real_targets[1] not in dict:
    #                     continue
    #                 res = real_targets[0] if real_targets[0] in dict else real_targets[1]
    #                 if res == b or res == a:
    #                     continue
    #                 print(f'{res} {a} {b}')
    #                 return res + a + b
    #         distance += 1

nums = [-13, 592, -501, 770, -952, -675, 322, -829, -246, 657, 608, 485, -112, 967, -30, 182, -969, 559, -286, -64, 24, 365, -158, 701, 535, -429, -217, 28, 948, -114, -536, -711, 693, 23, -958, -283, -700, -672, 311, 314, -712, -594, -351, 658, 747, 949, 70, 888, 166, 495, 244, -380, -654, 454, -281, -811, -168, -839, -106, 877, -216, 523, -234, -8, 289, -175, 920, -237, -791, -976, -509, -4, -3, 298, -190, 194, -328, 265, 150, 210, 285, -176, -646, -
        465, -97, -107, 668, 892, 612, -54, -272, -910, 557, -212, -930, -198, 38, -365, -729, -410, 932, 4, -565, -329, -456, 224, 443, -529, -428, -294, 191, 229, 112, -867, -163, -979, 236, -227, -388, -209, 984, 188, -549, 970, 951, -119, -146, 801, -554, 564, -769, 334, -819, -356, -724, -219, 527, -405, -27, -759, 722, -774, 758, 394, 146, 517, 870, -208, 742, -782, 336, -364, -558, -417, 663, -914, 536, 293, -818, 847, -322, 408, 876, -823, 827, 167]
target = 7175
tsc = ThreemSumClosest()
res = tsc.three_sum_closest(nums, target)
print(res)
