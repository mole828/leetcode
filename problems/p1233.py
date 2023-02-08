from typing import List

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        tree = {}
        for folder in folders:
            words = folder.split('/')[1:]
            node = tree
            for word in words:
                if word not in node:
                    node[word] = {}
                node = node[word]
            node[''] = {}
        print(tree)
        ans = []
        def dfs(node: dict)->list[str]:
            re = []
            if '' in node:return ['']
            for key in node.keys():
                re += ['/' + key + s for s in dfs(node[key])]
            if len(re)==0:return ['']
            # print(re)
            return re
        return dfs(tree)
        
    
if __name__ == '__main__':
    Solution().removeSubfolders(folders = ["/a","/a/b","/c/d","/c/d/e","/c/f"])