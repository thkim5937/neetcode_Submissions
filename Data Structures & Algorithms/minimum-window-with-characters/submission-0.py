class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need= {}
        for c in t:
            need[c] = need.get(c,0)+1
        have = 0
        total = len(need)
        l=0
        result = ""
        window={}
        for r in range(len(s)):
            c=s[r]
            window[c] = window.get(c,0)+1

            if c in need and window[c]==need[c]:
                have +=1
            
            while have==total:
                if not result or (r-l+1)<len(result):
                    result = s[l:r+1]
                window[s[l]]-=1
                if s[l] in need and window[s[l]]<need[s[l]]:
                    have-=1
                l+=1
        return result