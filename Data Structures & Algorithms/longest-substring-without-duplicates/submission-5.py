class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = 0

        arr = []
        for i in range(0, len(s), 1):
            if s[i] not in seen:
                seen.add(s[i])
                length+=1
            else:
                arr.append(length)
                length=1
                seen = set()
                k=i-1
                seen.add(s[i])
                while s[k]!= s[i]:
                    seen.add(s[k])
                    length+=1
                    k-=1
        arr.append(length);
        max=0
        for j in range(0, len(arr), 1):
            if arr[j]>max:
                max = arr[j]
        
        return max