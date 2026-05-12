class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # we need to calculate the sum of the first and second
        prefix = [1] * len(nums)
        pre = 1
        postfix = [1] * len(nums)
        post = 1

        for i in range(len(nums)):
            prefix[i] = pre 
            pre = nums[i] * pre

        for i in range(len(nums)-1, -1, -1):
            print(i)
            postfix[i] = post
            post = nums[i] * post

        ans = [1]*len(nums)
        for i in range(len(nums)):
            ans[i] = postfix[i] * prefix[i]

        return ans

            

