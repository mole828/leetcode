class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = [chr(ord('a')+dx) for dx in range(26)]
        dic = {' ':' '}
        for c in key:
            if c not in dic:
                dic[c] = d.pop(0)
        return ''.join([dic[c] for c in message])