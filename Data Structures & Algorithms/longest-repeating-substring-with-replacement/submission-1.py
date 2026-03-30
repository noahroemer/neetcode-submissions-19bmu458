class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = 0
        l = 0
        dic = {}
        
        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1

            
            while k + max(dic.values()) < (r - l + 1):
                dic[s[l]] -= 1
                l += 1
            curr = max(curr, r - l + 1)
        return curr
                
        

    
