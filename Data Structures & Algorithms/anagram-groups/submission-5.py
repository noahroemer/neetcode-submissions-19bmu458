from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # group all anagrams together.
        # dictionary with letters on left, and words on rights.
        dct = defaultdict(list)
        for word in strs:
            arr = [0]*26
            for letter in word:
                arr[ord(letter)-ord("a")] += 1
            dct[(tuple(arr))].append(word)

        return list(dct.values())
    
            

    
                