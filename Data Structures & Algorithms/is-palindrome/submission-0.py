class Solution:
    def isPalindrome(self, s: str) -> bool:
        com = "".join(c for c in s if c.isalnum())
        com = com.lower()
        L, R = 0, len(com)-1
        while L<R:
            if com[L]!=com[R]:
                return False
            else:
                L+=1
                R-=1
                continue
        return True
            