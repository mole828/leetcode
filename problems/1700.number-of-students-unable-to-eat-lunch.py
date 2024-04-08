#
# @lc app=leetcode id=1700 lang=python3
# @lcpr version=
#
# [1700] Number of Students Unable to Eat Lunch
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches[0] in students: 
            # print({
            #     'students':students,
            #     'sandwiches':sandwiches
            # })
            student = students.pop(0) 
            if student == sandwiches[0]: 
                sandwiches.pop(0) 
            else: 
                students.append(student) 
        return len(students)

# @lc code=end



#
# @lcpr case=start
# [1,1,0,0]\n[0,1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,1,0,0,1]\n[1,0,0,0,1,1]\n
# @lcpr case=end

#

