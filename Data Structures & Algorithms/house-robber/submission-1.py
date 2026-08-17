class Solution:
    def rob(self, nums: List[int]) -> int:
        # dynamic programming
        # base case: 1 house, just rob that
        # two houses: max(0, 1)
        # n houses: you can either rob house (n + n - 2) or rob (n - 1), take whichevery is greater
        if len(nums) == 1:
            return nums[0]
        one, two = 0, 0
        # start with house 3
        for i in range(len(nums)):
            temp = two
            two = max(nums[i] + one, two)
            one = temp
        
        return two