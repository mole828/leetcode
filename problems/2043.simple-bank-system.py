#
# @lc app=leetcode id=2043 lang=python3
# @lcpr version=30204
#
# [2043] Simple Bank System
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = {
            k+1: v for k,v in enumerate(balance)
        }

    def has(self, *ids: int) -> bool:
        for id in ids:
            if id not in self.balance:
                return False
        return True
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.has(account1, account2):
            return False
        if self.balance[account1] >= money:
            self.balance[account1] -= money
            self.balance[account2] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if not self.has(account):
            return False
        self.balance[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self.has(account):
            return False
        if self.balance[account] >= money:
            self.balance[account] -= money
            return True
        return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
# @lc code=end



