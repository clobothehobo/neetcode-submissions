class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = []
        s = s.lower()
        for a in s:
            if a.isalnum():
                x.append(a)
        print(x)
        for b in range(len(x)):
            if x[b] != x[len(x)-1-b]:
                return False
        return True