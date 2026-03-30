class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""

        for letter in s:
            if letter.isalnum():
                res += letter.lower()
        return res == res[::-1]
        
        
