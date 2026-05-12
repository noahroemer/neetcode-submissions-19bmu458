class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        l, r = 0, len(s1)
        s1dict = {}
        for letter in s1:
            s1dict[letter] = s1dict.get(letter, 0) + 1

        while r <= len(s2):
            st = s2[l:r]
            stdict = {}
            for letter in st:
                stdict[letter] = stdict.get(letter, 0) + 1
                
            l += 1
            r += 1

            if s1dict == stdict:
                return True
        return False                

        
            
        

            