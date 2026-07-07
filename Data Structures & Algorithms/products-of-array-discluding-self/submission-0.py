class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]*len(nums)
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
        right = [1]*len(nums)
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1]*nums[j+1]
        
        arr = [1]*len(nums)
        for k in range(len(nums)):
            arr[k] = left[k]*right[k]
        return arr