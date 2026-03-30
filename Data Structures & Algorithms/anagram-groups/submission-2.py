from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = defaultdict(list)

        for word in strs:
            letters = [0]*26
            for letter in word:
                letters[ord(letter) - ord("a")] += 1
            counts[tuple(letters)].append(word)
        return list(counts.values())