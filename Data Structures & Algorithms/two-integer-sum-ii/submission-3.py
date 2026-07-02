class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we must find the sum, index 1 must always be less than index 2
        # first thought is a left and a right pointer. if the current sume is too small, we move the left poiner


        # if it's too big we move the right pointer. 
        # so what we need to do is calculate the sum at each point in a while loop
        # then conditioned on k, determine which pointer to use
        # if it is greater than k we move the right pointer, less, left pointer

        l, r = 0, len(numbers) - 1

        while r > l:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

        