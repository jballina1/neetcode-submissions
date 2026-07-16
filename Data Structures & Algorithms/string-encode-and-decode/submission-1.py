class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ""
        for s in strs:
            ret = ret + str(len(s)) + "#" + s
        return ret

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_n = int(s[i:j])
            string = s[j + 1 : j + 1 + length_n]
            ret.append(string)
            i = j + 1 + length_n
        return ret
