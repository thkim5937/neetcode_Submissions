class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0] * 26
        for c in s:
            arr[ord(c) - 97] += 1
        for c in t:
            arr[ord(c) - 97] -= 1
        for count in arr:
            if count != 0:
                return False
        return True