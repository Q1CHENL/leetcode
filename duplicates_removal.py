# 1, 1, 1, 2, 3, 3, 4
class DuplicatesRemoval:
    # My original idea: del nums[i], which is expensive: O(N)
    # because of shifting every element
    #
    # def remove_duplicates(self, nums: list[int]) -> int:
    #     if len(nums) == 0:
    #         return 0
    #     if len(nums) == 1:
    #         return 1
    #     for i in range(0, len(nums)):
    #         if i >= len(nums)-1:
    #             return len(nums)
    #         while (i < len(nums) -1) and nums[i+1] == nums[i]:
    #             del nums[i+1]
                
    #     return len(nums)
    
    # From leetcode: two indices method:
    # insert unique number to the original list
    # i is always ahead of insertIndex so value of nums[i]
    # does not get affected by insertion
    def remove_duplicates(self, nums: list[int]) -> int:
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            # Found unique element
            if nums[i - 1] != nums[i]:      
                # Updating insertIndex in our main array
                nums[insertIndex] = nums[i] 
                # Incrementing insertIndex count by 1 
                insertIndex = insertIndex + 1       
        return insertIndex


a = [1, 1, 1, 2, 2, 3, 4, 4]
d = DuplicatesRemoval()
k = d.remove_duplicates(a)
print(k)
