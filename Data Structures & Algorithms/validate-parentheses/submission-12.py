class Solution:
    def isValid(self, s: str) -> bool:
        start = []
        bracks = {"(":")", "{":"}", "[":"]"}
        if len(s)%2 != 0:
            return False
        for b in s:
            if b in bracks:
                start.append(b)
            else:
                if(len(start)==0):
                    return False
                a = start.pop()
                if bracks[a]!=b:
                    return False
        if(len(start)!=0):
            return False
        return True
        
