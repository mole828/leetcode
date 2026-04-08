package problems.p3653
/*
 * @lc app=leetcode id=3653 lang=kotlin
 *
 * [3653] XOR After Range Multiplication Queries I
 */

// @lc code=start
const val MOD = 1_000_000_007L
class Solution {
    fun xorAfterQueries(nums: IntArray, queries: Array<IntArray>): Int {
        val longNums = nums.map { it.toLong() }.toMutableList()
        queries.forEach { query ->
            val (l, r, k, v) = query
            for (i in l..r step k) {
                longNums[i] = longNums[i] * v % MOD
            }
        }
        println(longNums)
        var result = 0L
        longNums.forEach { result = result xor it }
        return result.toInt()
    }
}
// @lc code=end

