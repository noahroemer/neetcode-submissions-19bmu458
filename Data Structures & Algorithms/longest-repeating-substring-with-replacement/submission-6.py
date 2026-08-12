class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # only uppercase english characters
        # so we have 26 possible letters
        # we can perform at most k replacemetns
        # so we should track the current window.
        # and in that window, track the letter that appears the most.
        # now we need to check that max + k <= len(window)
        # if it is less, we can move over the window on the right side
        # we will only ever move the window on the left side if max + k > len(window)
        # we will return the global max of len(window); need to track that 
        # need to define a counts arrary (for the letters)
        # variable of max (for letter)
        # variable of max (for length)

        counts = [0]*26
        max_letter = 0
        max_length = 0

        l = 0
        for r in range(len(s)):
            counts[ord(s[r]) - ord("A")] += 1
            max_letter = max(max_letter, counts[ord(s[r]) - ord("A")])

            # condition
            if max_letter + k >= (r-l+1):
                max_length = max(max_length, (r-l+1))

            else:
                counts[ord(s[l]) - ord("A")] -= 1
                l += 1
            
        return max_length



        

            


        