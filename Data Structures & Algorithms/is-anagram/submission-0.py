class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dict1 = {}
        dict2 = {}
        
        for i in range(len(s)):
            dict1[s[i]] = dict1.get(s[i], 0) + 1
        for i in range(len(t)):
            dict2[t[i]] = dict2.get(t[i], 0) + 1

        if dict1 == dict2:
            return True
        
        return False