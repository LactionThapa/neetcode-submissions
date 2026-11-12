class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        characters1 = {}
        characters2 = {}
        char = set()
        for i in s:
            if i in characters1:
                characters1[i] += 1
            else:
                characters1[i] = 1
                char.add(i)
        for i in t:
            if i in characters2:
                characters2[i] += 1
            else:
                characters2[i] = 1
        for i in char:
            if i in characters1 and i in characters2:
                if characters1[i] != characters2[i]:
                    return False
            else:
                return False
        return True

        
        