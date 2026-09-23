class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        hs = set()
        res = 0
        for r in range(len(s)):
            c = s[r]
            while hs and c in hs:
                hs.remove(s[l])
                l += 1
            hs.add(c)
            res = max(res, r - l + 1)
        return res