class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        one = [0]*26
        for c in s1:
            one[ord(c)-ord("a")] += 1

        l = 0
        two = [0]*26
        for r in range(len(s2)):
            two[ord(s2[r])-ord("a")] += 1
            print(two)
            if r-l+1 > len(s1):
                two[ord(s2[l])-ord("a")] -= 1
                l += 1
            if one == two:
                return True
        return False
                
        
            
        

            