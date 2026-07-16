class Solution:

    def encode(self, strs: List[str]) -> str:
        master = []
        for word in strs:
            for j in range(len(word)):
                master.append(str(ord(word[j])))
                master.append(".")
            master.append("-")
        return "".join(master)


    def decode(self, s: str) -> List[str]:
        out = []
        word = ""
        code = ""
        for i in range(len(s)):
            if s[i] == "-":
                out.append(word)
                word = ""
            elif s[i] == ".":
                word += chr(int(code))
                code = ""
            else:
                code += s[i]
        return out
            
            
                
            
