#
# @lc app=leetcode id=1352 lang=python3
# @lcpr version=30204
#
# [1352] Product of the Last K Numbers
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class ProductOfNumbers:

    def __init__(self):
        self.products = [1,]

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1,]
            return
        self.products.append(self.products[-1]*num)

    def getProduct(self, k: int) -> int:
        n = len(self.products)
        if k >= n:
            return 0
        return self.products[-1]//self.products[-1-k]
        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
# @lc code=end



