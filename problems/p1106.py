class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def function(s):
            s=s.replace("t","True")
            s=s.replace("f","False")
            s=s.replace("&","andfun")
            s=s.replace("|","orfun")
            s=s.replace("!","notfun")
            return s

        def andfun(*args):
            result=True
            for i in args:
                result=result and i
            return result

        def orfun(*args):
            result=False
            for i in args:
                result=result or i
            return result

        def notfun(a):
            return not a

        z=function(expression)
        return eval(z)