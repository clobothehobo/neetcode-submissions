class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        nstrs = {}
        for a in strs:
            na = "".join(sorted(a))
            if na in nstrs:
                nstrs[na].append(a)
            else:
                nstrs[na] = [a]
        return list(nstrs.values())

        
        