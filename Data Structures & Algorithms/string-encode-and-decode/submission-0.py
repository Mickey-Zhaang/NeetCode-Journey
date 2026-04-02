class Solution:

    def encode(self, strs: List[str]) -> str:
        en_string = ""

        for s in strs:
            en_string += "%" + s
        
        return en_string


    def decode(self, s: str) -> List[str]:
        return s[1:].split("%")
