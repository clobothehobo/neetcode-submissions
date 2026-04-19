class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        ht = {}
        for l in s:
            if l not in hs:
                hs[l] = 1
            else:
                hs[l] += 1
        for l in t:
            if l not in ht:
                ht[l] = 1
            else:
                ht[l] += 1

        if hs == ht:
            return True
        return False
