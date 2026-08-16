class Solution:
    def climbStairs(self, n: int) -> int:
        # dynamic programming: Start from stair n - 1, there is one way
        # stair n - 2, there are two ways
        # from stair n - 3, it would be (n - 1) + (n - 2), keep updating
        # you can also do it without recursion, just using a loop
        nxt = 1
        nxt_nxt = 2
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        for i in range(n - 2, 0, -1):
            total_ways = nxt + nxt_nxt
            nxt = nxt_nxt
            nxt_nxt = total_ways
        return total_ways    

        