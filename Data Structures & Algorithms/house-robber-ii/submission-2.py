class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic programming,similar to House Robber I
        # run the same algorithm with [0:n-1] and [1:n]
        # see which one you get maximum 
        if len(nums) == 1:
            return nums[0]
        def dp(array):
            one, two = 0, 0
            # start with house 3
            for num in array:
                temp = two
                two = max(num + one, two)
                one = temp
            
            return two
        return max(dp(nums[0:len(nums) - 1]), 
                    dp(nums[1:len(nums)]))
