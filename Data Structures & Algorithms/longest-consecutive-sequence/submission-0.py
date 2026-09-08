class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniques = set(nums)
        max_length = 0
        for n in nums:
            if n - 1 in uniques:
                continue
            start, cnt = n, 1
            while start + 1 in uniques:
                cnt += 1
                start += 1
            max_length = max(max_length, cnt)
        return max_length
        