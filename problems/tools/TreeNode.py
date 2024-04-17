
from typing import Optional, TypeVar, Generic
import warnings
from deprecated.sphinx import deprecated

warnings.filterwarnings('always')

T = TypeVar('T', int, str)

class TreeNode(Generic[T]):
    '''
    simple use TreeNode
    '''
    val: T
    left: 'TreeNode[T]'
    right: 'TreeNode[T]'
    def __init__(self, val:T=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"TreeNode({self.val})[{self.left},{self.right}]"
    
    @staticmethod
    def build(_array: list[Optional[T]]) -> Optional['TreeNode[T]']:
        '''
        build a Tree
        '''
        if len(_array) == 0:
            return None
        # print(array)
        root = TreeNode(_array.pop(0))
        que = [root]
        while _array:
            parent = que.pop(0)
            # print(root.val)
            v_left = _array.pop(0)
            if v_left:
                left = TreeNode(v_left)
                parent.left = left
                que.append(left)
            if _array:
                v_right = _array.pop(0)
                if v_right:
                    right = TreeNode(v_right)
                    parent.right = right
                    que.append(right)
            # print(parent)
        return root

@deprecated(reason="use TreeNode.build")
class TreeBuilder:
    @deprecated(reason="use TreeNode.build")
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
