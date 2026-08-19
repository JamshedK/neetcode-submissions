class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find algorithm
        par = [i for i in range(len(edges))]
        rank = [1] * len(edges)
        def find(n1):
            res = n1
            # keep looping until res is its own parent
            while res != par[res]:
                res = par[res]
            return res

        duplicate = [0]
        def union(n1, n2):
            # find their parents
            p1, p2 = find(n1), find(n2)

            # if parents are the same, means they have been connected before
            if p1 == p2:
                # print('same parents')
                duplicate[0] = [n1 + 1, n2 + 1]
            
            # otherwise, not connected yet, need to update their parents
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else: 
                par[p1] = p2
                rank[p2] += rank[p1]

        for a, b in edges:
            union(a-1, b-1)

        return duplicate[0]     
