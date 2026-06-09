class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={']':'[','}':'{',')':'('}
        for i in s:
            if i in check:
                if not stack or stack.pop()!=check[i]:
                    return False
            else:
                stack.append(i)
        return not stack
        