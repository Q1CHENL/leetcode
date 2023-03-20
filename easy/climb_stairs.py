from math import factorial


class ClimbStairs(object):
    # My solution: use combinatorics
    # for example IIIII, find ways of tuple II in III (5 gaps)
    # def climb_stairs(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     ways = 0
    #     gaps = n-1
    #     tuples = int(n/2)
    #     for tuple in range(1, tuples + 1):
    #         ways += factorial(gaps)/(factorial(tuple)*factorial(gaps-tuple))
    #         gaps -= 1
    #     return int(ways + 1) # plus all 1 step

    # From LeetCode: very clever method
    def climb_stairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # you can either climb it from the i - 1th stair 
        # by taking one step, or you can climb it from 
        # the i - 2th stair by taking two steps.
        # x: i-2
        # y: i-1
        # z: i
        y, z = 1, 2
        for _ in range(2, n):
            x = y
            y = z
            z = x + y

        return z

    # recursino like self.record[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    # works fine as well


cs = ClimbStairs()
ways = cs.climb_stairs(5)
print(ways)
