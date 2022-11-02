
"""
烂题, 不推荐
"""

from typing import List


class Solution(object):
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        """
        欧几里得距离：两点间的线段距离
        """
        import math
        def calQ(x,y,radius):
            res=0
            for xi,yi,qi in towers:
                d=math.sqrt((xi-x)**2+(yi-y)**2)
                #信号外的点不要算进来，一开始我都看漏了这个radius
                if d<=radius:
                    res+=int(float(qi)/(1+d))
            return res
        #↓信号最强的点一定在这些点构成的矩阵中间，找出矩阵范围
        xmin,ymin=50,50
        xmax,ymax=0,0
        for pos in towers:
            xmin,ymin=min(xmin,pos[0]),min(ymin,pos[1])
            xmax,ymax=max(xmax,pos[0]),max(ymax,pos[1])
        #↓遍历矩阵所有点
        signal=0
        ans=[0,0]
        #↑这里不设置ans=[xmin,ymin]的原因是测试用例有信号强度为0的情况
        #↑当塔信号强度为0，此时[x,y]最小的非负坐标就是原点[0,0]
        for i in range(xmin,xmax+1):
            for j in range(ymin,ymax+1):
                tmp=calQ(i,j,radius)
                if tmp>signal:
                    signal=tmp
                    ans=[i,j]
        return ans