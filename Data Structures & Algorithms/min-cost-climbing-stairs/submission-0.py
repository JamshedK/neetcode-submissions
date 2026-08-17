class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # if at the last step, minimum is cost[i]
        # if at the last step before cost[i]
        # minimum step at step i: cost[i] + min(cost[i + 1], cost[i + 2])
        # we can use the input array 
        # [1,2,1,2,1,1,1] last_index = len(n) - 1
        if len(cost) == 1:
            return cost[0]
        
        # start at the last_index - 2 element
        last_index = len(cost) - 1
        for i in range(last_index - 2, -1, -1):
            cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])
        
        return min(cost[0], cost[1])