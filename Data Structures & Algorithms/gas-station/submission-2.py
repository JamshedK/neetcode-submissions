class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # brute force solution
        if sum(gas) < sum(cost):
            return - 1
        
        r = 0
        start = 0
        while r < len(gas):
            # keep going until you have enough gas
            curr_gas = 0
            while r < len(gas) and curr_gas >= 0:
                # print(f'travelling from {gas[r]}')
                curr_gas += gas[r] - cost[r]
                r += 1
            if r != len(gas):
                # print('not reached end yet')
                # update start 
                start = r
        return start - 1 if start == len(gas) else start