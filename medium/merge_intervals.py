# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping
# intervals, and return an array of the non-overlapping intervals that cover all the
# intervals in the input.

# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]] Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
from typing import List

class Merger:
    # My Solution
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        intervals.sort() # no need for propagation if sorted
        non_overlapping = []
        non_overlapping.append([intervals[0][0], intervals[0][1]])
        for i in intervals[1:]:
            if self.overlapped(non_overlapping[-1], i):
                # don't even need to update [0] if sorted
                # non_overlapping[-1][0] = min(non_overlapping[-1][0], i[0]) 
                non_overlapping[-1][1] = max(non_overlapping[-1][1], i[1])                
                # self.propagate_back(non_overlapping)
            else:
                non_overlapping.append([i[0], i[1]])
        return non_overlapping
    
    def overlapped(self, interval1, interval2) -> bool:
        return interval2[0] >= interval1[0] and interval2[0] <= interval1[1]
    
    # def propagate_back(self, intervals):
    #     curr = intervals[-1]
    #     for i in intervals[:][::-1][1:]:
    #         if self.overlapped(curr, i):
    #             intervals[-1] = [min(curr[0], i[0]), max(curr[1], i[1])]
    #             intervals.remove(i)
    #             curr = intervals[-1]

mgr = Merger()


i1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
res1 = mgr.merge(i1)
print(res1)

i2 = [[1, 4], [1, 4]]
res2 = mgr.merge(i2)
print(res2)

i3 = [[1, 4], [2, 3]]
res3 = mgr.merge(i3)
print(res3)

i4 = [[1, 4], [0, 0]]
res4 = mgr.merge(i4)
print(res4)

i5 = [[1,4],[0,2],[3,5]]
res5 = mgr.merge(i5)
print(res5)


i6 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
res6 = mgr.merge(i6)
print(res6)

i7 = [[2,3],[5,5],[2,2],[3,4],[3,4]]
res7 = mgr.merge(i7)
print(res7)

        
        

