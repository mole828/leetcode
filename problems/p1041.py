class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        y,x = 0,0
        dy,dx=1,0
        for _ in range(4):
            for c in instructions:
                if c=="G":
                    y += dy
                    x += dx
                if c=="L":
                    dy,dx = dx,-dy
                if c=="R":
                    dy,dx = -dx,dy 
            if y==0 and x==0: return True
        return False