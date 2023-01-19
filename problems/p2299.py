import re


class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        return all([
            len(password) >= 8,
            re.search("[a-z]", password),
            re.search("[A-Z]", password),
            re.search("[0-9]", password),
            re.search("[!@#$%^&*()+-]", password),
            not re.search(r"(.)\1{1}", password)
        ])