#
# @lc app=leetcode id=1948 lang=python3
# @lcpr version=30204
#
# [1948] Delete Duplicate Folders in System
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import defaultdict
import hashlib
from typing import List

# 定义树节点结构
class Node:
    children: dict[str, "Node"]
    def __init__(self):
        self.children = dict()
        self.id = -1  # 唯一id

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node()
        node_id = [0]

        # Step 1: 构建文件夹树结构
        for path in paths:
            curr = root
            for folder in path:
                if folder not in curr.children:
                    curr.children[folder] = Node()
                    curr.children[folder].id = node_id[0]
                    node_id[0] += 1
                curr = curr.children[folder]

        # Step 2: 使用哈希值进行序列化
        serial_map = defaultdict(list)

        def serialize(node: Node):
            if not node.children:
                return "#" 
            items = []
            for name in sorted(node.children):
                sub_serial = serialize(node.children[name])
                items.append(f"{name}:{sub_serial}")
            raw = "|".join(items)
            hashed = hashlib.md5(raw.encode()).hexdigest()
            serial_map[hashed].append(node)
            return hashed

        serialize(root)

        deleted = set()
        for hash_val, nodes in serial_map.items():
            if len(nodes) > 1:
                for node in nodes:
                    deleted.add(node)

        ans = []

        def collect(node: Node, path: List[str]):
            for name, child in node.children.items():
                if child in deleted:
                    continue
                new_path = path + [name]
                ans.append(new_path)
                collect(child, new_path)

        collect(root, [])
        return ans

# @lc code=end



#
# @lcpr case=start
# [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]\n
# @lcpr case=end

# @lcpr case=start
# [["a","b"],["c","d"],["c"],["a"]]\n
# @lcpr case=end

#

