class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for x in s:
            count[x] = count.get(x,0) + 1
        for y in t:
            count[y] = count.get(y,0) - 1
        for values in count.values():
            if values != 0:
                return False

        return True