class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        preMul, postMul = [1 for _ in range(length)], [1 for _ in range(length)]
        # calculate all preMul
        curr = 1
        for i in range(1, length):
            preMul[i] = curr * nums[i-1]
            curr = preMul[i]
        
        # calculate all post_mul
        curr = 1
        for i in range(length - 2, -1, -1):
            postMul[i] = curr * nums[i + 1]
            curr = postMul[i]
        # print(preMul)
        # print(postMul)
        res = []
        for i in range(length):
            res.append(preMul[i] * postMul[i])
        return res