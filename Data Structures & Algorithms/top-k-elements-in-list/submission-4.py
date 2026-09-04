class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # import heapq
        # from collections import Counter
        # cnt = [(freq, val) for val, freq in Counter(nums).items()]
        # h = cnt[:k]
        # heapq.heapify(h)
        # for freq, val in cnt[k:]:
        #     if freq > h[0][0]:
        #         heapq.heappushpop(h, (freq, val))
        # return [val for _, val in h]
        from collections import Counter
        cnt = [(freq, val) for val, freq in Counter(nums).items()]
        buckets = [[] for _ in range(len(nums)+1)]
        for freq, val in cnt:
            buckets[freq].append(val)
        results = []
        i = len(buckets) - 1
        while i >= 0:
            while buckets[i]:
                results.append(buckets[i].pop())
                k -= 1
                if not k:
                    return results
            i -= 1
        return results

        