
from typing import Optional


class TreeNode: 
    val: int 
    left: 'TreeNode' 
    right: 'TreeNode' 
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode({self.val})[{self.left},{self.right}]"

class TreeBuilder:
    def build(array: list[Optional[int]]) -> Optional[TreeNode]:
        if len(array) == 0:
            return None 
        print(array)
        root = TreeNode(array.pop(0))
        que = [root]
        while array:
            parent = que.pop(0)
            # print(root.val)
            vLeft = array.pop(0)
            if vLeft:
                left = TreeNode(vLeft)
                parent.left = left 
                que.append(left)
            if array:
                vRight = array.pop(0)
                if vRight:
                    right = TreeNode(vRight)
                    parent.right = right
                    que.append(right)
            # print(parent)
        return root
    
    # def print(node: Optional[TreeNode]):


null = None 
if __name__ == '__main__':
    array = [1,2,null,3,null,4,null,5]
    print(TreeBuilder.build(array))
