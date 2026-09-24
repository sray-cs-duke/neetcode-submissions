class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for c in s:
            if c.isalnum():
                filtered += c.lower()
        l = 0
        r = len(filtered) - 1

        while l < r:
            if filtered[l] != filtered[r]:
                return False
            l += 1
            r -= 1
        
        return True