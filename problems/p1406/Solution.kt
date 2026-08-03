package p1406

/*
 * @lc app=leetcode id=1406 lang=kotlin
 *
 * [1406] Stone Game III
 */

// @lc code=start
class Solution {
    fun stoneGameIII(stoneValue: IntArray): String {
        val n = stoneValue.size
        val memo = IntArray(n+1) { Int.MIN_VALUE }
        fun dfs(i: Int): Int {
            if(i==n)return 0
            val cacheValue = memo[i]
            if(cacheValue != Int.MIN_VALUE)return cacheValue
            var res = Int.MIN_VALUE
            var s = 0
            for(j in i..<minOf(i+3,n)){
                s += stoneValue[j]
                res = max(res, s-dfs(j+1))
            }
            memo[i] = res
            return res
        }
        val diff = dfs(0)
        if (diff==0) return "Tie"
        return if(diff>0) "Alice" else "Bob"
    }
}
// @lc code=end

