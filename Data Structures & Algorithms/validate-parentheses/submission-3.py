class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={']':'[','}':'{',')':'('}
        for i in s:
            if i in ']})':
                if stack:
                    if check[i]==stack[-1]:
                        stack.pop()
                    else:
                        return False
                else: return False
            else:
                stack.append(i)
        if not stack:
            return True
        return False
        