class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programming
        # base case: 1 house, just rob that
        # two houses: max(0, 1)
        # n houses: you can either rob house (n + n - 2) or rob (n - 1), take whichevery is greater
        last_index = len(nums) - 1
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[1], nums[0])

        # start with house 3
        for i in range(2, len(nums)):
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1])
        
        return nums[last_index]