# There is a robot on an m x n grid. The robot is initially
# located at the top-left corner (i.e., grid[0][0]). The
# robot tries to move to the bottom-right corner
# (i.e., grid[m - 1][n - 1]). The robot can only move either
# down or right at any point in time.

# Given the two integers m and n, return the number of
# possible unique paths that the robot can take to reach the
# bottom-right corner.

# The test cases are generated so that the answer will be #
# less than or equal to 2 * 109.
# [robot_maze.png]
import math


class PathFinder:
    # Simple but Time exceeded solution
    # def unique_paths(self, m: int, n: int) -> int:
    #     if m <= 1 or n <= 1:
    #         return 1
    #     return self.unique_paths(m-1, n) + self.unique_paths(m, n-1)

    # This problem can be seen as a classic math problem:
    # Total fixed step length: m + n
    # We need to decide in each step if we take right/down, which
    # leads to C(m+n, m)( == C(m+n, n) ), where C is the math combination
    # The sequence is not considered here because every right/down is the same

    # It means out of m+n steps we MUST choose m steps to move right
    # and n steps to move down

    # More precisely, it takes (m-1)+(n-1) = m+n-2 steps in total
    def unique_paths(self, m: int, n: int) -> int:
        # return math.factorial(m+n-2) // (math.factorial(m-1) * math.factorial(n-1))
        return math.comb(m+n-2, m-1)

    # A dynamic programming approach
    def unique_paths_dp(self, m: int, n: int) -> int:
        # You initialize a 2D array dp where dp[i][j] will eventually contain the number
        # of unique paths from (0, 0) to (i, j). Initially, the top row (i == 0) and the
        # left column (j == 0) are set to 1 because there's only one way to get to any
        # of these points: by moving right along the top row or moving down along the left column.
        dp = [[1 if i == 0 or j ==
               0 else 0 for j in range(n)] for i in range(m)]

        # You loop through the 2D array starting from (1, 1) because the first row and the
        # first column are already initialized. For each cell (i, j), you calculate the number
        # of unique paths to that cell by adding the number of unique paths to the cell above it
        # (dp[i-1][j]) and to the cell to the left of it (dp[i][j-1]).
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        # Finally, you return dp[-1][-1], which contains the number of unique paths from (0, 0)
        # to (m-1, n-1) — the bottom-right corner of the grid.
        return dp[-1][-1]


pf = PathFinder()
m = 20
n = 20
res = pf.unique_paths(m, n)
print(res)
# add path 3 by 3: 3 x 2


# Excursion

# Divide-and-conquer and dynamic programming (DP) are both algorithmic paradigms used for solving problems,
# and they do share similarities, such as breaking problems down into smaller parts. However, they are
# generally considered to be distinct approaches due to key differences.

# Divide-and-Conquer:
# Non-overlapping Subproblems: Divide-and-conquer typically breaks the problem into non-overlapping
# subproblems. For example, in merge sort, the array is divided into two non-overlapping subarrays.

# No Memoization: Solutions to subproblems are usually not stored for future use.

# Recursion: This paradigm often makes heavy use of recursion to divide the problem into subproblems, solve
# each one, and then combine them.

# Dynamic Programming:
# Overlapping Subproblems: DP breaks problems into subproblems that often overlap. This is why memoization
# or tabulation is beneficial.

# Memoization/Tabulation: Solutions to subproblems are stored to avoid redundant calculations.

# Optimization: DP is often used for optimization problems where the best solution is sought, rather than
# just any solution.

# State Transition: DP often has a state transition relation that shows how to build up the solution to a
# problem based on solutions to smaller problems.

# Where They Intersect:
# There are some problems for which both paradigms can be applied, often resulting in different algorithms
# with different efficiency characteristics. For example, the Fibonacci sequence can be computed using a
# straightforward divide-and-conquer algorithm that has exponential time complexity, or it can be computed
# using dynamic programming to achieve linear time complexity.

# In summary, while divide-and-conquer and dynamic programming both involve breaking problems down into smaller
# subproblems, the methods they use and the types of problems they are applied to can be quite different.
