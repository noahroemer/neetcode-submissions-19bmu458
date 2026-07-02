class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res = [1] * len(nums)
        postfix = [1] * len(nums)
        prefix = [1] * len(nums)
        pre = 1
        post = 1
        

        for i, n in enumerate(nums):
            prefix[i] *= pre
            pre *= n
        for i, n in reversed(list(enumerate(nums))):
            postfix[i] *= post
            post *= n

        print(prefix, postfix)
        for i in range(len(postfix)):
            res[i] = prefix[i] * postfix[i]
        return res
            
        