class Solution:
    def isValid(self, s: str) -> bool:
        start = []
        bracks = {"(":")", "{":"}", "[":"]"}
        for b in s:
            if b in bracks:
                start.append(bracks[b])
            else:
                if len(start)==0:
                    return False
                a = start.pop()
                if a!=b:
                    return False
        if len(start)!=0:
            return False
        return True
