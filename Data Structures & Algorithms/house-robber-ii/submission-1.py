class Solution:
    def rob(self, nums: List[int]) -> int:
        # Dynamic programming,similar to House Robber I
        # run the same algorithm with [0:n-1] and [1:n]
        # see which one you get maximum 
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        nums1 = nums[0:len(nums)-1]
        nums2 = nums[1:len(nums)]
        # print(nums1, nums2)
        memoize = []
        memoize = memoize + [nums1[0], max(nums1[0], nums1[1])]

        for i in range(2, len(nums1)):
            max_val = max(nums1[i] + memoize[i - 2], memoize[i - 1])
            memoize.append(max_val)
        max_val1 = memoize[-1]

        # print(memoize)
        memoize[0] = nums2[0]
        memoize[1] = max(nums2[1], nums2[0])
        for i in range(2, len(nums2)):
            memoize[i] = max(nums2[i] + memoize[i - 2], memoize[i - 1])
        max_val2 = memoize[-1]
        # print(memoize)
        return max(max_val1, max_val2)


