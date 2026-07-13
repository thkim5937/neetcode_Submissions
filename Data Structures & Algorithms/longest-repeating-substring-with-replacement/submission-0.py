class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l=0
        max_count=0
        result=0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r],0)+1
            max_count = max(max_count, seen[s[r]])

            if r-l+1-max_count >k:
                seen[s[l]]-=1
                l+=1
            result = max(result, r-l+1)
        return result