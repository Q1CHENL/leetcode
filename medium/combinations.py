from typing import List
from itertools import combinations

class Combi:
    # My recursive solution, works but slow
    def combine(self, n: int, k: int) -> List[List[int]]:
        numbers = [i for i in range(1, n+1)]
        
        def impl(nums, k):
            if k == 1:
                return [[j] for j in nums]
            tmp_ret = []
            for i in range(len(nums)+1-k):
                tmp_combis = impl(nums[i+1:], k-1)
                for tc in tmp_combis:
                    tmp_ret.append([nums[i]] + tc)
            return tmp_ret
                
        ret = impl(numbers, k)
        return ret
    
    # Fast leetcode sample solution: backtrack
    def combine_backtrack(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(curr, first):
            if len(curr) == k:
                ans.append(curr[:])
                return

            need = k - len(curr)
            remain = n - first + 1 
            available = remain - need
            for num in range(first, first+available+1):
                curr.append(num)
                backtrack(curr, num+1)
                curr.pop()

            return
    
        backtrack([],1)
        return ans
    
    # Built-in function: most fast
    def combine_builtin(self, n: int, k: int) -> List[List[int]]:
        return list(combinations(range(1, n+1), k))
    

cb = Combi()
# res = cb.combine(20, 10)
# res = cb.combine_backtrack(20, 10)
res = cb.combine_builtin(20, 10)
# print(res)
[1, 2, 3, 4]
            