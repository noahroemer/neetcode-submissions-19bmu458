class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max_length = 0
        seen = set()

        l, r = 0, 0

        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            seen.add(s[r])

            curr = r - l + 1
            max_length = max(curr, max_length)
            
            r += 1
        return max_length
    


    




            
        



        
            