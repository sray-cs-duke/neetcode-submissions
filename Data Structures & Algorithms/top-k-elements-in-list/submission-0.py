class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = 0
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        items = list(count.items())
        items.sort(key=lambda pair: pair[1], reverse=True)

        res = []

        for i in range(k):
            res.append(items[i][0])

        return res