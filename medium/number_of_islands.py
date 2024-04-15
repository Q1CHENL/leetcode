from typing import List
class Solution:
    # check_matrix is inspired by leetcode solutions
    # original impl used list and could not pass the last case: Time Exceeded
    def numIslands(self, grid: List[List[str]]) -> int:
        check_matrix = [[False for j in range(len(grid[0]))] for i in range(len(grid))]
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '0': continue
                if check_matrix[i][j] == True: continue
                num = num + 1
                self.find_all_connected_lands([i, j], grid, 1, check_matrix)
        return num
    
    def find_all_connected_lands(self, pos, grid, direction_to_prev, check_matrix):
        if (grid[pos[0]][pos[1]] == '0'):
            return
        if check_matrix[pos[0]][pos[1]] == False:
            check_matrix[pos[0]][pos[1]] = True
        else: 
            return
        for i in range(1, 5):
            if i != direction_to_prev:
                if i == 1 and pos[1] > 0:
                    self.find_all_connected_lands([pos[0], pos[1] - 1], grid, 3, check_matrix)
                elif i == 2 and pos[0] > 0:
                    self.find_all_connected_lands([pos[0] - 1, pos[1]], grid, 4, check_matrix)
                elif i == 3 and pos[1] + 1 < len(grid[0]):
                    self.find_all_connected_lands([pos[0], pos[1] + 1], grid, 1, check_matrix)
                elif i == 4 and pos[0] < len(grid) - 1:
                    self.find_all_connected_lands([pos[0] + 1, pos[1]], grid, 2, check_matrix)

IslandsCounter = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# an extreme case would be: 360000x300
num = IslandsCounter.numIslands(grid)
print(num)