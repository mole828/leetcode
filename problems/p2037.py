from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum(abs(c[0]-c[1]) for c in zip(sorted(seats),sorted(students)))

if __name__ == '__main__':
    print(Solution().minMovesToSeat(seats = [3,1,5], students = [2,7,4]))