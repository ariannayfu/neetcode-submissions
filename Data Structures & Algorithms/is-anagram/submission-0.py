class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sChars = {}
        tChars = {}
        for ch in s:
            if ch in sChars:
                sChars[ch] += 1
            else:
                sChars[ch] = 1
        for ch in t:
            if ch in tChars:
                tChars[ch] += 1
            else: 
                tChars[ch] = 1
        for key, value in sChars.items():
            if (key not in tChars) or (tChars[key] != value):
                return False
        return True
