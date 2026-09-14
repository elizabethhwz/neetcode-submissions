class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < n and k > i and j < k:
                if j >= i + 2 and nums[j] == nums[j-1]:
                    j += 1
                    continue
                if k < n - 1 and nums[k] == nums[k+1]:
                    k -= 1
                    continue
                if nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                elif nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
        return res
                
        