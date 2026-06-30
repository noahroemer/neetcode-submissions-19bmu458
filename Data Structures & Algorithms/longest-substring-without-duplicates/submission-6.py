class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # initialize our variables
        max_len = 0
        l = 0
        charSet = set()

        for r in range(len(s)): 
            # check if in the set first
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])

            max_len = max(max_len, r - l + 1)

        return max_len



            # if it isn't in the set let's add it
            
        
        


    




            
        



        
            