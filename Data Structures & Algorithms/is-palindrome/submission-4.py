class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for x in s:
            if x.isalnum():
                clean += x.lower()
        if clean == clean[::-1]:
            return True
        return False