class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j < len(s):
            if s[j].isnumeric():
                j += 1
                continue
            elif s[j] == "#":
                length = int(s[i:j])
                if not length:
                    res.append("")
                    i = j + 1
                else:
                    i = j + 1
                    if i < len(s) and i + length <= len(s):
                        res.append(s[i:i + length])
                i += length
                j = i
        return res
