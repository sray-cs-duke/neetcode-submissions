class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for x in s:
            if x.isalnum():
                filtered += x.lower()
        if filtered == filtered[::-1]:
            return True
        return False