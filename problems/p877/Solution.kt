package p877
/*
 * @lc app=leetcode id=877 lang=kotlin
 *
 * [877] Stone Game
 */
// @lc code=start
class Solution {
    fun stoneGame(piles: IntArray): Boolean {
        val memo = Array(piles.size) { IntArray(piles.size) }
        fun dfs(l: Int, r: Int): Int {
            if (l == r) return piles[l]
            if (memo[l][r] != 0) return memo[l][r]
            val a = piles[l] - dfs(l + 1, r)
            val b = piles[r] - dfs(l, r - 1)
            memo[l][r] = maxOf(a, b)
            return memo[l][r]
        }
        return dfs(0, piles.size - 1) >= 0
    }
}
// @lc code=end

