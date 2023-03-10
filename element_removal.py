class ElementRemoval:
    def remove_element(self, nums: list[int], val: int) -> int:
        insertIndex = 0
        for num in nums:
            if num != val:
                # Avoid redundant insertions
                if nums[insertIndex] != num:
                    nums[insertIndex] = num
                insertIndex += 1
        return insertIndex


nums = [3, 2, 2, 3]
nums1 = [0, 1, 2, 2, 3, 0, 4, 2]
e = ElementRemoval()
e.remove_element(nums, 3)
print(nums)
