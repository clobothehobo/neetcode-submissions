class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCharacters = {}
        tCharacters = {}
        for char in s:
            if char not in sCharacters:
                sCharacters[char] =1
            else:
                sCharacters[char] +=1
        for char in t:
            if char not in tCharacters:
                tCharacters[char] = 1
            else:
                tCharacters[char] +=1
        if sCharacters == tCharacters:
            return True
        else:
            return False
