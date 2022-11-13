class Solution(object):
    def customSortString(self, order:str, s:str):
        return ''.join(sorted(list(s), key=lambda x:order.find(x)))