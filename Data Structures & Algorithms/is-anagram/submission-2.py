class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        characters = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in characters:
                characters[i] += 1
            else:
                characters[i] = 1
        for i in t:
            if i in characters:
                if characters[i] == 0:
                    return False
                characters[i] -= 1
            else:
                return False
        return True
        