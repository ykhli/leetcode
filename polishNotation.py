class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        sym = ["+", "-","*","/"]
        tokens = list(tokens)
        stack = []
        for i in tokens:
            if i not in sym:
                stack.insert(0,float(i))
            else:
                if tokens.index(i) == 0:
                    print "ERROR"
                    return -1
                else:
                    item1 = stack.pop(0)
                    item2 = stack.pop(0)                    
                    if i == "+":
                        stack.insert(0,int(item1)+item2)
                    elif i == "-":
                        stack.insert(0,int(item2)-item1)
                    elif i == "*":
                        stack.insert(0,int(item2)*item1)
                    elif i == "/":
                        stack.insert(0,int(item2*1.0/item1))



                        
        return stack[0]
                
if __name__ == "__main__":
    x = Solution()
    print x.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
                
                
