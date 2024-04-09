from typing import List
class Trapper:
    def trap_through(self, height: List[int]) -> int:
        trapped_amount = 0
        # idea: 2 ptr
        left = 0
        # forward left to the first trap's left side
        for i in range(len(height)):
            if i < len(height) - 1 and height[i] > height[i + 1]:
                left = i
                break
        right = left + 1
        
        while right < len(height):
            if right + 1 > len(height) and height[right] > height[right - 1]:
                trapped_amount = trapped_amount + self.collect_water(left, right, height)
                break
            if (right + 1 < len(height) and height[right - 1] < height[right] and height[right] >= height[right + 1]) or (right == len(height) - 1 and height[right] > height[right - 1]):
                trapped_amount = trapped_amount + self.collect_water(left, right, height)
                left = right
                right = right + 1
            else:
                right = right + 1    
        return height, trapped_amount
                    
    def collect_water(self, left, right, height) -> int:
        min_of_lr = min(height[left], height[right])
        collected = 0
        for i, h in enumerate(height[left + 1: right]):
            if min_of_lr > h:
                collected = collected + (min_of_lr - h)
                height[left + i + 1] = min_of_lr
        return collected
    
    def trap(self, height: List[int]) -> int:
        total = 0
        while True:
            height, amount1 = self.trap_through(height)
            total = total + amount1
            if amount1 == 0:
                break
        return total

    # Idea from X: @Yangxcasear
    # def trap(self, height: List[int]) -> int:
    #     max_height = max(height)
    #     layer = []
    #     trapped = 0
    #     for i in range(max_height):
    #         for h in height:
    #             if h >= i + 1:
    #                 layer.append(1)
    #             else:
    #                 layer.append(0)
    #         layer = self.remove_trailing_and_leading_zeros(layer)
    #         trapped = trapped + layer.count(0)
    #         layer = []
    #     return trapped
    
    # def remove_trailing_and_leading_zeros(self, lst):
    #     start = 0
    #     end = len(lst)
    #     # Find the index of the first non-zero element from the start
    #     while start < end and lst[start] == 0:
    #         start += 1
    #     # Find the index of the first non-zero element from the end
    #     while end > start and lst[end - 1] == 0:
    #         end -= 1
    #     return lst[start:end]

    
tpr = Trapper()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
trapped1 = tpr.trap(height)
print(f"Trapped water amount1: {trapped1}")

height2 = [4,2,0,3,2,5]
trapped2 = tpr.trap(height2)
print(f"Trapped water amount2: {trapped2}")

height3 = [5,4,1,2]
trapped3 = tpr.trap(height3)
print(f"Trapped water amount3: {trapped3}")

height4 = [6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3]
trapped4 = tpr.trap(height4)
print(f"Trapped water amount4: {trapped4}")

height5 = [8,8,1,5,6,2,5,3,3,9]
trapped5 = tpr.trap(height5)
print(f"Trapped water amount5: {trapped5}")
