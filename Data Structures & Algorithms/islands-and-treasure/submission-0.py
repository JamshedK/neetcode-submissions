from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # let's first try a single source BFS

        rows, cols = len(grid), len(grid[0])
        visited = set()
        def bfs():
            level = 1
            while q: 
                temp = []
                for _ in range(len(q)):
                    r, c = q.popleft()
                    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                    for dr, dc in directions: 
                        row, col = r + dr, c + dc
                        # mark the position if it's land
                        if (row in range(rows)
                                and col in range(cols)
                                and (row, col) not in visited
                                and grid[row][col] == 2147483647):
                            visited.add((row, col))
                            grid[row][col] = level
                            q.append((row, col))
                level += 1
        q = deque([])
        for r in range(rows):
            for c in range(cols):
                # only search if r, c is 0
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        bfs()
        

        