class Solution:

    def encode(self, strs: List[str]) -> str:
        ret = ''
        for s in strs:
            ret += f'#{len(s)}#'
            ret += s
        print(ret)
        return ret
    def decode(self, s: str) -> List[str]:
        return re.split(r'#\d+#',s)[1:]
        