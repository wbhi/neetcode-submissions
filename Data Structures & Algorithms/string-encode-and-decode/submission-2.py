class Solution:

    def encode(self, strs: List[str]) -> str:
        self.res=""
        for i in strs:
            self.res+='#@'+i
        return self.res

        

    def decode(self, s: str) -> List[str]:
        return self.res.split("#@")[1:]
