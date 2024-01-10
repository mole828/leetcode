
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeBuilder:
    def build(array: list[Optional[int]]) -> TreeNode:
        root = TreeNode(array.pop(0))
        que = [root]
        while array:
            root = que.pop(0)
            # print(root.val)
            vLeft = array.pop(0)
            if vLeft:
                left = TreeNode(vLeft)
                root.left = left 
                que.append(left)
            if not array:
                break 
            vRight = array.pop(0)
            if vRight:
                right = TreeNode(vRight)
                root.right = right
                que.append(right)

            # node.left = TreeNode(next(cur))
            # node.right = TreeNode(next(cur))
        return root

null = None 
if __name__ == '__main__':
    array = [1,2,null,3,null,4,null,5]
    TreeBuilder(array)