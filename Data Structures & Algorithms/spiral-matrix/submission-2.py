class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []
        while left <= right and top <= bottom: 
            # take the top row, and keep increasing left
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1
            # take the right column, but starting from top + 1
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            if top <= bottom and left <= right:
                # take bottom row
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                # take the left column, but skip top and bottom row
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
            # left += 1
            # right -= 1
            # top += 1
            # bottom -= 1
            # print('shifted')
        return res