package p1331
/*
 * @lc app=leetcode id=1331 lang=kotlin
 *
 * [1331] Rank Transform of an Array
 */
// @lc code=start
class Solution {
    fun arrayRankTransform(arr: IntArray): IntArray {
        val ranks = arr
            .distinct()
            .sorted()
            .withIndex()
            .associate { (rank, num) -> num to rank + 1 }

        return arr.map { ranks.getValue(it) }.toIntArray()
    }
}
// @lc code=end
