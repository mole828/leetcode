package p2267

/*
 * @lc app=leetcode id=2267 lang=kotlin
 *
 * [2267]  Check if There Is a Valid Parentheses String Path
 */

// @lc code=start
class Solution {
    fun hasValidPath(grid: Array<CharArray>): Boolean {
        val row = grid.size
        val col = grid.first().size
        val memo = mutableMapOf<Triple<Int,Int,Int>, Boolean>()
        fun dfs(y: Int, x: Int, deep: Int): Boolean {
            // println("dfs(y=$y,x=$x,deep=$deep)")
            if (y >= row || x >= col) return false
            if (deep < 0) return false
            val char = grid[y][x]
            val nextDeep = deep + if (grid[y][x] == '(') 1 else -1
            if (y == row - 1 && x == col - 1) return nextDeep == 0
            val key = Triple(y, x, deep)
            return memo[key]?.let { return it } ?: run {
                val res = dfs(y+1, x, nextDeep) || dfs(y, x+1, nextDeep)
                memo[key] = res
                res
            }
        }
        return dfs(0,0,0)
    }
}
// @lc code=end

