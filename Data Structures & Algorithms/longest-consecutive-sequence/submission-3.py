class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # array won't work nums are too big
        # use a hashmap
        # look through and if the difference matches or smtn?  we need to get them all in order
        # so for exampes
        # we need to sort the dictionary
        # from there enumerate the keys and values, this should only be one pass
        # this isn't even, we should just sor the array
        if not nums:
            return 0
            
        numset = set(nums)
        max_len = 1

        for num in nums:
            curr_len = 1
            curr = num
            while (curr + 1) in numset:
                curr_len += 1
                curr += 1
            max_len = max(max_len, curr_len)

        return max_len         



            
