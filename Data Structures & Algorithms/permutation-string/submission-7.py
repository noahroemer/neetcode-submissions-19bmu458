class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        # first hashmap
        map1 = {}
        for letter in s1:
            map1[letter] = map1.get(letter, 0) + 1
        print(map1)

        # sliding window; keep same length as s1
        n = len(s1)
        
        for i in range(len(s2)):
            if i+n <= len(s2):
                temp = s2[i:i+n]
                map2 = {}
                for letter in temp:
                    map2[letter] = map2.get(letter, 0) + 1
                print(map2)
                if map2 == map1:
                    return True
        return False
        
            
                

        
            
        

            