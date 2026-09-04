class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        from collections import Counter
        cnt = [(freq, val) for val, freq in Counter(nums).items()]
        h = cnt[:k]
        heapq.heapify(h)
        for freq, val in cnt[k:]:
            if freq > h[0][0]:
                heapq.heappushpop(h, (freq, val))
        return [val for _, val in h]
            
        