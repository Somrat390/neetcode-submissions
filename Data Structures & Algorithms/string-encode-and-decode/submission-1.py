class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        new_str = ""
        for i in strs:
            list_str = str(len(i)) + "#" + i
            new_str += list_str
        return new_str
        


    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        strs = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            strs.append(s[j:j+length])

            i = j + length
        return strs
        
        

