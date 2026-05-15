class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        pre = post = 1
        res = [1]*len(nums)

        for i in range(len(nums)):
            prefix[i] = pre 
            pre *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            postfix[i] = post
            post *= nums[i]
        print(prefix, postfix)
        for i in range(len(nums)):
            res[i] = prefix[i]*postfix[i]
            

        return res
