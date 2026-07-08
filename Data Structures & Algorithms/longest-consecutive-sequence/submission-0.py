class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        max_len = 0
        for i in nums:
            if (i-1) not in seen:
                n=0
                while (i+n) in seen:
                    n+=1
                max_len = max(max_len, n)
        return max_len