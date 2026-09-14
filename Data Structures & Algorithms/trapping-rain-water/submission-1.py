class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        # pref = 0
        # prefix = []
        # for h in height:
        #     pref = max(pref, h)
        #     prefix.append(pref)
        
        # suf = 0
        # suffix = [0] * n
        # for i in range(n - 1, -1, -1):
        #     suf = max(suf, height[i])
        #     suffix[i] = suf
        
        # total = 0
        # for p, s, h in zip(prefix, suffix, height):
        #     total += min(p, s) - h
        # return total
    
        l, r = 0, n - 1
        leftMax, rightMax, total = 0, 0, 0
        while l < r:
            leftMax = max(leftMax, height[l])
            rightMax = max(rightMax, height[r])
            if leftMax <= rightMax:
                total += leftMax - height[l]
                l += 1
            else:
                total += rightMax - height[r]
                r -= 1
        return total
        
        

        
        