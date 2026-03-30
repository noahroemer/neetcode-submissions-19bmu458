from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # we should make a hashmap that tracks letters value, and the words key. 
        words_map = defaultdict(list)
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            words_map[tuple(counts)].append(word)
        return list(words_map.values())

    
                