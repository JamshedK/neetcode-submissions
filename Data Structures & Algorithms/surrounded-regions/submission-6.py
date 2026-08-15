class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Goal: DFS, start with border regions, visit all other nodes from there and then board
        def dfs(row, col):
            if (row < 0 or row >= ROWS
                    or col < 0 or col >= COLS
                    or board[row][col] == 'X'  
                    or (row, col) in visited):
                return 
            visited.add((row, col))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            for dr, dc in directions: 
                r, c = row + dr, col + dc
                dfs(r, c)

        def replace_zeros(hashset):
            for (r, c) in hashset: 
                board[r][c] = 'X'

        ROWS, COLS = len(board), len(board[0])
        visited = set()
        # go through first and last row
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS-1, i)
        
        # go through first and last column
        for i in range(ROWS):
            dfs(i, 0)
            dfs(i, COLS-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited: 
                    board[r][c] = 'X'


        