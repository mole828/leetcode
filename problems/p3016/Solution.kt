package p3016
/*
 * @lc app=leetcode id=3016 lang=kotlin
 *
 * [3016] Minimum Number of Pushes to Type Word II
 */
// @lc code=start
class Solution {
    fun minimumPushes(word: String): Int {
        val count = IntArray(26)
        for (c in word) count[c - 'a']++
        val nums = count.filter { it > 0 }
        return nums.sortedDescending().mapIndexed { i, c ->
            c * (i / 8 + 1)
        }.sum()
    }
}
// @lc code=end

