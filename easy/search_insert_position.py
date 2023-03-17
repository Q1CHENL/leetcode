class SearchInsertPosition:
    def search_insert(self, nums: list[int], target: int) -> int:
        if len(nums) == 0: return 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
    
si = SearchInsertPosition()
nums = [1, 3, 5, 6]
index = si.search_insert(nums, 7)
print(index)        
        