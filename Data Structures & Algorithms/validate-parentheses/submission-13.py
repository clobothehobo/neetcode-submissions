class Solution:
    def isValid(self, s: str) -> bool:
        start = []
        bracks = {"(":")", "{":"}", "[":"]"}
        for b in s:
            if b in bracks:
                start.append(b)
            elif len(start)==0:
                return False
            else:
                a = start.pop()
                if bracks[a]!=b:
                    return False
        if(len(start)!=0):
            return False
        return True
        
