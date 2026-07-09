package p3532

/*
 * @lc app=leetcode id=3532 lang=kotlin
 *
 * [3532] Path Existence Queries in a Graph I
 */

// @lc code=start
class Solution {
    fun pathExistenceQueries(n: Int, nums: IntArray, maxDiff: Int, queries: Array<IntArray>): BooleanArray {
        val group = IntArray(n)
        for (i in 1 until n) {
            group[i] = group[i - 1]
            if (nums[i] - nums[i - 1] > maxDiff) {
                group[i]++
            }
        }

        return queries.map { (u, v) -> group[u] == group[v] }.toBooleanArray()
    }
}
// @lc code=end

fun main() {
    
}
