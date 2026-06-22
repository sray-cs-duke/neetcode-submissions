class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len (t):
            return False
        counter = 0
        count = {}
        for x in s:
            count[x] = count.get(x, 0) + 1

        for y in t:
            count[y] = count.get(y, 0) - 1

        for value in count.values():
            if value != 0:
                return False

        return True
