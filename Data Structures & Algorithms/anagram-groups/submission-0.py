from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = defaultdict(list)
        

        for word in strs:
            sorted_word = tuple(sorted(word))

            dict[sorted_word].append(word)

        return list(dict.values())