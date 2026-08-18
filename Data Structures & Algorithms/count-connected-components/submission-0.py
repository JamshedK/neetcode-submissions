class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        
        for a, b in edges: 
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj_list[node]:
                dfs(nei)
        
        visited = set()
        count = 0
        for i in range(n):
            if i not in visited: 
                dfs(i)
                count += 1
        return count