package p1111

/*
 * @lc app=leetcode id=1111 lang=kotlin
 *
 * [1111] Maximum Nesting Depth of Two Valid Parentheses Strings
 */

// @lc code=start
class Solution {
    fun maxDepthAfterSplit(seq: String): IntArray {
        val ans = IntArray(seq.length)
        var deep = 0
        seq.forEachIndexed { i, char->
            when (char) {
                '(' -> {
                    ans[i] = deep%2
                    deep += 1
                }
                ')' -> {
                    deep -= 1
                    ans[i] = deep%2
                }
                else -> error("?")
            }
        }
        return ans
    }
}
// @lc code=end

