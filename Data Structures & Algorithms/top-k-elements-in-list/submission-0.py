class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] = d[num] + 1
        d_sorted = sorted(d.items(), key=lambda item: item[1], reverse=True)
        l = []
        for i in range(k):
            l.append(d_sorted[i][0])
        return l