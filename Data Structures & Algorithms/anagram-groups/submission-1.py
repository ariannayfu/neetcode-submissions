class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def checkMapsSame(sChars, tChars) -> bool:
            if len(sChars) != len(tChars):
                return False
            for key, value in sChars.items():
                if (key not in tChars) or (tChars[key] != value):
                    return False
            return True
        
        def createMap(s) -> dict:
            sChars = {}
            for ch in s:
                if ch in sChars:
                    sChars[ch] += 1
                else:
                    sChars[ch] = 1
            return sChars
        
        words = []
        maps = []
        for wrd in strs:
            charMap = createMap(wrd)
            found = False
            for idx, m in enumerate(maps):
                if checkMapsSame(charMap, m):
                    #found match, add in
                    words[idx].append(wrd)
                    found = True
            if not found:
                maps.append(charMap)
                words.append([wrd])
        return words

        