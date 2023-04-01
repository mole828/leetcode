class Solution:
    def maskPII(self, s:str):
        idx = s.find("@")
        if idx != -1:
            s = s.lower()
            tmp = s[:idx]
            return tmp[0]+"*"*5+tmp[-1]+s[idx:]
        else:
            s = [x for x in s if x.isdigit()]
            n = len(s)
            if n == 10:
                return "*"*3+"-"+"*"*3+"-"+"".join(s[-4:])
            else:
                return "+"+"*"*(n-10)+"-"+"*"*3+"-"+"*"*3+"-"+"".join(s[-4:])