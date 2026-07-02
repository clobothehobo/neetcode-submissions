class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}
        for l in s:
            if l not in sDict:
                sDict[l] = 1
            else:
                sDict[l] += 1
        for l in t:
            if l not in tDict:
                tDict[l] = 1
            else:
                tDict[l] += 1
        if sDict == tDict:
            return True
        return False
        