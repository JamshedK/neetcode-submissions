class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) -1
        left, right = 0, len(matrix[0]) - 1
        target_row = -1
        while top <= bottom:
            middle = (top + bottom) // 2
            print(middle)
            # check if target is is within the middle
            if matrix[middle][0] <= target and target <= matrix[middle][-1]:
                target_row = middle
                print(f'Found row {target_row + 1}')
                break
            # if target is less than the first column of middle
            elif target < matrix[middle][0]:
                print(f'Row {middle + 1} is less than target')
                bottom = middle - 1
            # if target is bigger than the last column of middle
            else: 
                top = middle + 1
        
        if target_row == -1:
            return False

        while left <= right:
            mid = (left + right) // 2
            if matrix[target_row][mid] == target:
                return True
            # if middle is smaller
            if target < matrix[target_row][mid]:
                right = mid - 1
            # else target is bigger than middle
            else:
                left = mid + 1
        return False