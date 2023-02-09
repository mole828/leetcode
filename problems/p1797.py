class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.veri_code = dict()


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.veri_code[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.veri_code or self.veri_code[tokenId] <= currentTime:
            return
        self.veri_code[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return sum(v > currentTime for v in self.veri_code.values())