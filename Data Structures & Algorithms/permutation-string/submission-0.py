class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = [0] * 26
        for c in s1:
            freq1[ord(c) - ord("a")] += 1
        
        l, r = 0, len(s1)
        freq2 = [0] * 26
        for c in s2[l:r]:
            freq2[ord(c) - ord("a")] += 1

        while r < len(s2):
            if freq1 == freq2:
                return True
            freq2[ord(s2[l]) - ord("a")] -= 1
            freq2[ord(s2[r]) - ord("a")] += 1
            l += 1
            r += 1
            
        return freq1 == freq2            
