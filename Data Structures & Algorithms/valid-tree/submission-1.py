class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Goal: Detect that there are no cycles and all the nodes are connected
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            p = n1
            while par[n1] != n1: 
                n1 = par[n1] 
            return n1
        
        def union(n1, n2):
            p1, p2 =  find(n1), find(n2)
            # if parents are the same, skip 
            if p1 == p2: 
                return False
            # otherwise, connect them using whichever has a greater rank
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else: 
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges:
            if union(n1, n2) == False: 
                return False
        
        return len(edges) == n - 1
