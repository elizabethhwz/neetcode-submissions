class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter, defaultdict
        cntT = Counter(t)
        cntS = defaultdict(int)
        matches, need = 0, len(cntT)
        minL = float('inf')
        res = ""
        l, r = 0, 0
        for r, c in enumerate(s):
            cntS[c] += 1
            if c in cntT and cntS[c] == cntT[c]:
                matches += 1
            while matches == need:
                if r - l + 1 < minL:
                    minL = r - l + 1
                    res = s[l:r+1]
                cl = s[l]
                cntS[cl] -= 1
                if cl in cntT and cntS[cl] < cntT[cl]:
                    matches -= 1
                l += 1

        return res
        