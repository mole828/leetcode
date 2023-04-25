from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [name for _,name in sorted( zip(heights,names) ,reverse=True)]
    

if __name__ == '__main__':
    print(Solution().sortPeople(names = ["Mary","John","Emma"], heights = [180,165,170]))