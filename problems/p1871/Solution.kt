/*
 * @lc app=leetcode id=1871 lang=kotlin
 *
 * [1871] Jump Game VII
 *
 * https://leetcode.com/problems/jump-game-vii/description/
 *
 * algorithms
 * Medium (26.26%)
 * Likes:    1855
 * Dislikes: 122
 * Total Accepted:    73.6K
 * Total Submissions: 268.1K
 * Testcase Example:  '"011010"\n2\n3'
 *
 * You are given a 0-indexed binary string s and two integers minJump and
 * maxJump. In the beginning, you are standing at index 0, which is equal to
 * '0'. You can move from index i to index j if the following conditions are
 * fulfilled:
 * 
 * 
 * i + minJump <= j <= min(i + maxJump, s.length - 1), and
 * s[j] == '0'.
 * 
 * 
 * Return true if you can reach index s.length - 1 in s, or false otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "011010", minJump = 2, maxJump = 3
 * Output: true
 * Explanation:
 * In the first step, move from index 0 to index 3. 
 * In the second step, move from index 3 to index 5.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "01101110", minJump = 2, maxJump = 3
 * Output: false
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= s.length <= 10^5
 * s[i] is either '0' or '1'.
 * s[0] == '0'
 * 1 <= minJump <= maxJump < s.length
 * 
 * 
 */
package p1871

// @lc code=start
class Solution {
    @Deprecated("Memory Limit Exceeded")
    fun canReach0(s: String, minJump: Int, maxJump: Int): Boolean {
        fun canJump(i: Int): List<Int> {
            return (i + minJump..minOf(i + maxJump, s.lastIndex))
            .filter { s[it] == '0' }
        }
        val hasMeet = BooleanArray(s.length)
        var layer = listOf(0)
        while (layer.isNotEmpty()) {
            val nextLayer = mutableListOf<Int>()
            layer.forEach { from -> 
                if (hasMeet[from]) return@forEach
                if (from == s.length - 1) return true 
                canJump(from).forEach { nextLayer.add(it) }
                hasMeet[from] = true
            }
            layer = nextLayer
        }
        return false
    }

    fun canReach(s: String, minJump: Int, maxJump: Int): Boolean {
        val n = s.length
        if (s[n - 1] != '0') return false

        val dp = BooleanArray(n)
        dp[0] = true

        var reachableCount = 0

        for (i in 1 until n) {
            val add = i - minJump
            if (add >= 0 && dp[add]) reachableCount++

            val remove = i - maxJump - 1
            if (remove >= 0 && dp[remove]) reachableCount--

            dp[i] = s[i] == '0' && reachableCount > 0
        }

        return dp[n - 1]
    }
}
// @lc code=end

