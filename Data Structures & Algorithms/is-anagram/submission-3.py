class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram = {}
        for char_s, char_t in zip(s,t):
            anagram[char_s] = anagram.get(char_s,0)+1
            anagram[char_t] = anagram.get(char_t, 0) - 1
        for k in anagram:
            if anagram[k] != 0:
                return False
        return True
            
              
            
       