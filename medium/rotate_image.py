from typing import List

# You are given an n x n 2D matrix representing an image, rotate
# the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to
# modify the input 2D matrix directly. DO NOT allocate another
# 2D matrix and do the rotation.

# Example: [rotate_image.jpg]


class Rotation:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side_len = len(matrix) # from 0 to the middle
        row_start = 0
        iter = side_len // 2 + 1
        for i in range(iter):
            curr_row = matrix[i]
            for j in range(row_start, side_len - 1 - row_start):
                curr_elem = curr_row[j]
                
                tmp_0 = matrix[j][side_len - 1 - row_start]
                matrix[j][side_len - 1 - row_start] = curr_elem

                tmp_1 = matrix[side_len - 1 - row_start][side_len - 1 - j]
                matrix[side_len - 1 - row_start][side_len - 1 - j] = tmp_0

                tmp_2 = matrix[side_len - 1 - j][i]
                matrix[side_len - 1 - j][i] = tmp_1

                curr_row[j] = tmp_2
                
            row_start += 1


rt = Rotation()
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix1 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rt.rotate(matrix1)
print(f"{matrix1}: {matrix1 == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]}")
