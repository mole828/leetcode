/*
 * @lc app=leetcode id=2379 lang=kotlin
 * @lcpr version=30204
 *
 * [2379] Minimum Recolors to Get K Consecutive Black Blocks
 */


// @lcpr-template-start

// @lcpr-template-end
package leetcode.problem_2379
// @lc code=start
class Solution {
    enum class Color {
        WHITE, BLACK
    }
    fun minimumRecolors(blocks: String, k: Int): Int {
        val list = blocks.map{if(it == 'B') Color.BLACK else Color.WHITE}.toMutableList()
        var left = 0
        var right = k
        val count = list.subList(left, right).groupBy { it }.mapValues { it.value.size }.toMutableMap()
        var minWhite = count[Color.WHITE] ?: run {
            return@minimumRecolors 0
        }
        while (right < list.size) {
            println("sub: ${list.subList(left, right)}")
            count.set(list[left], count.getOrDefault(list[left], 0) - 1)
            count.set(list[right], count.getOrDefault(list[right], 0) + 1)
            minWhite = minOf(minWhite, count[Color.WHITE]!!)
            right += 1
            left += 1
        }
        return minWhite
    }
}
// @lc code=end

fun main() {
    println(Solution().minimumRecolors("WBBWWBBWBW", 7))
    println(Solution().minimumRecolors("WBWBBBW", 2))
    println(Solution().minimumRecolors("WBB", 1))
}


/*
// @lcpr case=start
// "WBBWWBBWBW"\n7\n
// @lcpr case=end

// @lcpr case=start
// "WBWBBBW"\n2\n
// @lcpr case=end

 */

