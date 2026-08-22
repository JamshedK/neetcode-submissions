class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        # move 1: matrix[top][left] -> matrix[top][right]
        # move 2: matrix[top][right] -> matrix[bottom][right]
        # move 3: matrix[bottom][right] -> matrix[bottom][left]
        # move 4: matrix[bottom][left] -> matrix[top][left]
        # after all these moves are done, you shrink top and bottom 
        n = len(matrix)
        while top <= bottom and left <= right:
            for i in range(n - 1):
                temp1 = matrix[top + i][right]
                # move 1
                matrix[top + i][right] = matrix[top][left + i]
                # move 2
                temp2 = matrix[bottom][right - i]
                matrix[bottom][right - i] = temp1
                # move 3
                temp3 = matrix[bottom - i][left]
                matrix[bottom - i][left] = temp2
                # move 4
                matrix[top][left + i] = temp3
                # print(matrix[top][left], matrix[top][right], matrix[bottom][right], matrix[bottom][left])
            # update n and the pointers
            n -= 2
            top += 1
            bottom -= 1
            left += 1
            right -= 1