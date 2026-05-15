class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we need to make a sliding window hashmap type thibg
        # track the length, max count and then add 2

        # r - l + 1 -   -maxcount <= 2
        
        l, r = 0, 0 

        counts = [0]*26
        max_len = 0

        while r < len(s):
            counts[ord(s[r])-ord("A")] += 1
            while ((r-l+1) - max(counts)) > k:
                counts[ord(s[l])-ord("A")] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
            print(max_len)
            r += 1
           

        return max_len

