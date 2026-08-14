from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        def add_room(r, c):
            if (r not in range(rows)
                    or c not in range(cols)
                    or (r, c) in visited
                    or grid[r][c] == -1):
                return 
            visited.add((r, c))
            q.append((r, c))
        
        q = deque([])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        level = 0
        while q: 
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = level
                add_room(r - 1, c)
                add_room(r + 1, c)
                add_room(r, c - 1)
                add_room(r, c + 1)
            level += 1
        

        