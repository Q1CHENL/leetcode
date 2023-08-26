class Permutation(object):
    # From CharGPT:
    # hard part is, why it covers all permutations
    # Main idea is that, though permuations are too many, there is still a pattern:
    # for example [1, 2, 3]: all permutations = all permutations starting with 1 +
    #                                           all permutations starting with 2 +
    #                                           all permutations starting with 3

    # to obtain e.g all permutations starting with 1, we need all permutations of [2, 3],
    # which is again equals all permutations starting with 2 + all permutations starting with 3
    # and so on and so forth
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return [[]]

        result = []

        # this lines ensure that every elem and the rest will be gone through
        for i in range(len(nums)):
            # for example: [1, 2, 3]
            # in the first iteration: nums[i] = 1, rest = [2, 3]
            # the returned list contains every permutation starting with 1
            rest = nums[:i] + nums[i+1:]
            for p in self.permute(rest):
                # here is the "real" calculation:
                # current start and every permuation of rest is combined
                result.append([nums[i]] + p)
        return result


permuter = Permutation()
nums = [1, 2, 3]  # 4, 5, 6]
res = permuter.permute(nums)
print(res)
