class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)  
        rows = {i: set() for i in range(n)}
        cols = {j: set() for j in range(n)}
        for row in range(3):
            for col in range(3):
                box = set()
                # loop through the small box
                for i in range(3):
                    for j in range(3):
                        # calculate the idx for small box
                        row_idx = row * 3 + i
                        col_idx = col * 3 + j
                        # print(row_idx, col_idx)
                        # get the value and convert to int
                        if board[row_idx][col_idx] == '.':
                            continue
                        number = int(board[row_idx][col_idx])
                        # if already exists in box, return False
                        if (number in box) or (number in rows[row_idx]) or (number in cols[col_idx]):
                            return False
                        box.add(number)
                        rows[row_idx].add(number)
                        cols[col_idx].add(number)
                # print(f"Current row {row_idx}")
                # print(rows)
                # print(cols)
                # print("\n------")
        return True
