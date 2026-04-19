class Solution:
    def isValid(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        stack = []
        for c in s:
            if c in open:
                stack.append(c)
            else:
                if(stack):
                    a = stack.pop()
                    if open.index(a) == close.index(c):
                        continue
                    else:
                        return False
                else:
                    return False
        if(stack):
            return False
        return True