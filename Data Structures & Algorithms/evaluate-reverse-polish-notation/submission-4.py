class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        res=0
        for i in tokens:
            if i not in '-*/+':
                stack.append(int(i))
            else:
                if i=='+':
                    stack.append(stack.pop()+stack.pop())
                if i=='-':
                    stack.append(-(stack.pop())+stack.pop())
                if i=='/':
                    a=stack.pop()
                    b=stack.pop()
                    if a!=0:
                        stack.append(int(b/a))
                if i=='*':
                    stack.append((stack.pop())*(stack.pop()))
        return stack[0]

        