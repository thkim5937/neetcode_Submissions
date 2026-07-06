class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for n in nums:
            if n in seen:
                seen[n]+=1
            else:
                seen[n]=1
        arr=[]
        for _ in range(len(nums)+1):
            arr.append([])
        for val, freq in seen.items():
            arr[freq].append(val)
        result = []
        for i in range(len(arr)-1, 0, -1):
            for val in arr[i]:
                result.append(val)
                if len(result)==k:
                    return result
        return result