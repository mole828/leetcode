package problems.p2751
/*
 * @lc app=leetcode id=2751 lang=kotlin
 *
 * [2751] Robot Collisions
 */

// @lc code=start
class Solution {
    fun survivedRobotsHealths(positions: IntArray, healths: IntArray, directions: String): List<Int> {
        val n = positions.size
        // 1. 创建索引数组并按位置排序，模拟 Python 的 sorted(range(n), key=...)
        val indices = Array(n) { it }
        indices.sortBy { positions[it] }

        val stack = mutableListOf<Int>()

        for (i in indices) {
            if (directions[i] == 'R') {
                stack.add(i)
            } else {
                while (stack.isNotEmpty() && healths[stack.last()] < healths[i]) {
                    healths[i] -= 1
                    healths[stack.removeLast()] = 0
                }
                
                if (stack.isNotEmpty()) {
                    if (healths[stack.last()] == healths[i]) {
                        healths[stack.removeLast()] = 0
                    } else {
                        healths[stack.last()] -= 1
                    }
                    healths[i] = 0
                }
            }
        }

        return healths.filter { it > 0 }
    }
}
// @lc code=end

