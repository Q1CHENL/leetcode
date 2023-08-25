class Searcher(object):
    # My solution: find breakpoint and do bin search in the correct range
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        breakpoint = self.find_breakpoint(nums)
        if target < nums[length - 1]:
            left = breakpoint
            right = len(nums) - 1
        elif target > nums[length - 1]:
            left = 0
            right = breakpoint - 1
        else:
            return length - 1
        index = self.bin_search(nums[left: right + 1], target)
        return index + left if index != -1 else -1

    def bin_search(self, nums, target):
        found = False
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                found = True
                return mid
            mid = (left + right) // 2
        return mid if found else -1

    def find_breakpoint(self, nums):
        if nums[len(nums) - 1] > nums[0]:
            return 0
        first = nums[0]
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left < right - 1:
            if nums[mid] > first:
                left = mid
            else:
                right = mid
            mid = (left + right) // 2
        return right

    # Sample from leetcode: straightforward and faster
    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     l = 0
    #     r = len(nums) - 1
    #     while l <= r:
    #         mid = (r+l) / 2
    #         if target == nums[mid]:
    #             return mid
    #         # left part is sorted 
    #         if nums[mid] >= nums[l]:
                  # target is not in left part
    #             if target < nums[l] or target > nums[mid]:
    #                 l = mid+1
                  # target is in left part
    #             else:
    #                 r = mid-1
              # right part is sorted
    #         else:
    #             if target > nums[r] or target < nums[mid]:
    #                 r = mid-1
    #             else:
    #                 l = mid+1
    #     return -1
                
            
sr = Searcher()
# nums = [4, 5, 6, 7, 0, 1, 2 ]
nums = [3, 1]
bp = sr.find_breakpoint(nums)
print(f"break: {bp}")
index = sr.search(nums, 0)
print(f"index: {index}")
