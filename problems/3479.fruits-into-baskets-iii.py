#
# @lc app=leetcode id=3479 lang=python3
#
# [3479] Fruits Into Baskets III
#

# @lc code=start
from typing import List


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        for fruit in fruits:
            for i, basket in enumerate(baskets):
                if basket >= fruit:
                    baskets[i] = 0
                    break
        return sum(1 for b in baskets if b)
    
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        stack = [(0, baskets[0])]
        for i, v in enumerate(baskets):
            if v > stack[-1][1]:
                stack.append((i, v))
        
        for fruit in fruits:
            # find should begin
            should_begin = False
            begin_at = 0
            for i, basket_in_stack in stack:
                if basket_in_stack >= fruit:
                    should_begin = True
                    begin_at = i
                    break
                else:
                    begin_at = i
            if should_begin:
                for i in range(begin_at, len(baskets)):
                    basket = baskets[i]
                    if basket >= fruit:
                        baskets[i] = 0
                        break
                    
        print(stack)
        print(baskets)
        return sum(1 for b in baskets if b)
    
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(baskets)
        class ValueNode:
            father: 'MaxNode'
            value: int
            def __init__(self, value: int):
                self.value = value
                self.father = None
            def change(self, value: int):
                self.value = value
                if self.father:
                    self.father.son_change(self)
        class MaxNode(ValueNode):
            left: ValueNode
            right: ValueNode
            def __init__(self, left: ValueNode, right: ValueNode):
                self.value = max(left.value, right.value)
                self.father = None
                self.left = left
                self.right = right
                self.left.father = self
                self.right.father = self
            def son_change(self, son: ValueNode):
                self.change(max(self.left.value, self.right.value))
        
        floors = [[ValueNode(v) for v in baskets]]
        while len(floors[-1]) > 1:
            next_floor = [MaxNode(floors[-1][2*i], floors[-1][2*i+1]) for i in range(len(floors[-1]) // 2)] 
            if len(floors[-1]) % 2 == 1:
                next_floor.append(floors[-1][-1])
            floors.append(next_floor)

        root = floors[-1][0]

        change_times = 0
        for fruit in fruits:
            node = root
            if node.value >= fruit:
                while isinstance(node, MaxNode):
                    if node.left.value >= fruit:
                        node = node.left
                    else:
                        node = node.right
                node.change(0)
                change_times += 1
        return n - change_times


        
# @lc code=end

# print(Solution().numOfUnplacedFruits([3,6,1], [6,4,7]))
# print(Solution().numOfUnplacedFruits([4,2,5], [3,5,4]))
# print(Solution().numOfUnplacedFruits([4], [4]))