class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = ("").join(char for char in s if char.isalnum())
        b = a.lower()
        for i in range(len(b)//2):
            if b[i]!=b[len(b)-1-i]:
                return False
        return True