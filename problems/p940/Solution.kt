package p940

/*
 * @lc app=leetcode id=940 lang=kotlin
 *
 * [940] Distinct Subsequences II
 */

// @lc code=start
private const val MOD = 1_000_000_007L
class Solution {
    @Deprecated("time limit exceeded")
    fun distinctSubseqII0(s: String): Int {
        fun dfs(i: Int): Set<String> {
            if (i == s.length) return emptySet()
            val next = dfs(i + 1)
            val result = mutableSetOf<String>()
            for (str in next) {
                result.add(str)
                result.add(s[i] + str)
            }
            result.add(s[i].toString())
            return result
        }
        return dfs(0).size
    }
    fun distinctSubseqII(s: String): Int {
        /*
            a   b
        a   1   0   ('a')
        b   1   2   ('a', 'b', 'ab')
        a   4   2   ('a', 'b', 'ab', 'aa', 'ba', 'aba')
        */
        val f = LongArray(26) { 0 }
        for (c in s) {
            f[c - 'a'] = (f.sum() + 1) % MOD
        }
        return (f.sum() % MOD).toInt()
    }
}
// @lc code=end

