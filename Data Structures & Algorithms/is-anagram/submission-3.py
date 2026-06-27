class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = {}
        for x in s:
            counter[x] = counter.get(x,0) + 1
        for y in t:
            counter[y] = counter.get(y,0) - 1
        for values in counter.values():
            if values != 0:
                return False
        return True