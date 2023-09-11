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

class PathFinder:
    # Time exceeded solution
    # def unique_paths(self, m: int, n: int) -> int:
    #     if m <= 1 or n <= 1:
    #         return 1
    #     return self.unique_paths(m-1, n) + self.unique_paths(m, n-1)
    def unique_paths(self, m: int, n: int) -> int:
        pass

pf = PathFinder()
m = 10
n = 10
res = pf.unique_paths(m, n)
print(res)
# add path 3 by 3: 3 x 2
 