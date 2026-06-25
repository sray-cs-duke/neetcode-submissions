class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
        
        item = list(count.items())
        item.sort(key=lambda pair:pair[1], reverse = True)

        res = []
        for i in range(k):
            res.append(item[i][0])
        return res

