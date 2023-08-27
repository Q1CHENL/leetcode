# What is Backtracking?
# Backtracking is a general algorithm for finding all (or some) solutions to computational 
# problems, particularly constraint satisfaction problems. It incrementally builds 
# candidates for solutions, but abandons a candidate ("backtracks") as soon as it 
# determines that it cannot be extended to a valid solution. The classic metaphor for 
# backtracking is that of a maze: you want to find a path out, but you may have to go down 
# a few wrong paths before you find the right one.

# Why is it Called "Backtracking"?
# The name "backtracking" comes from the idea that when you reach a point where you cannot 
# proceed any further (a dead end), **you backtrack to the most recent point where you have 
# the option to make a different choice**.

# Is This a Classic Example of Backtracking?
# Yes, the "Combination Sum" problem is a classic example of backtracking. You start by 
# selecting one element from the list and then proceed to find a combination that sums up 
# to the remaining target. If you can't find such a combination, you backtrack and try 
# another element. This process is repeated recursively until all possible combinations 
# are found.

from typing import List
# Given an array of distinct integers candidates and a target integer target, return a
# list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two
# combinations are unique if the frequency of at least one of the chosen numbers
# is different.

# The test cases are generated such that the number of unique combinations that sum up to
# target is less than 150 combinations for the given input.


class CombiSum(object):
    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path, res):
            # start: The index to start the for-loop in the candidates list.
            # target: The remaining sum we are trying to reach.
            # path: The current combination of numbers we have chosen.
            # res: The result list that stores all unique combinations.

            # We found a valid combination
            if target == 0:
                # add current combination to result
                res.append(path)
                return
            # if target is not 0, we loop through the remaining candidates
            # and make recursive call to "backtrack"
            # we start not always from 0 to prevent duplicates
            for i in range(start, len(candidates)):
                # skip the numbers that would make the sum exceed the target
                if candidates[i] > target:
                    continue
                # the actual "probing" happens here: path + [candidates[i]]
                backtrack(i, target - candidates[i], path + [candidates[i]], res)

                # in the first test case, path will fall from [2, 2, 2] back to [2, 2] after return because [2, 2, 2] + [2]/[3]/[6]/[7] will exceed
                # then proceed to next *iteration*(because backtrack is the last call in for loop) starting to try [2, 2] + [3] since 3 is candidate[i=0+1]

                # after trying [2, 2, 6], [2, 2, 7], the path will return to sole [2] since [2, 2, x] is not possible anymore: which mean double 2 + any other
                # number is not possible, so we start to try with single 2

        res = []
        backtrack(0, target, [], res)
        return res
    
# it also works for candidates that is not sorted:
# if a combination is possible using a number that appears before the current starting
# index, then that combination would have already been explored and added to the result
# set when the earlier number was the starting point for the recursion.


combiSum = CombiSum()

# Example 1
print(combiSum.combination_sum([6, 7, 3, 2], 9))
# Output: [[2, 2, 3], [7]]

# Example 2
print(combiSum.combination_sum([2, 3, 5], 8))
# Output: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

# Example 3
print(combiSum.combination_sum([2], 1))
