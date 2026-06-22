package p1189

/*
 * @lc app=leetcode id=1189 lang=kotlin
 *
 * [1189] Maximum Number of Balloons
 */

// @lc code=start
class Solution {
    fun maxNumberOfBalloons(text: String): Int {
        val count = IntArray(26)
        for (c in text) {
            count[c - 'a']++
        }
        
        return minOf(
            count['b' - 'a'], 
            count['a' - 'a'], 
            count['l' - 'a'] / 2, 
            count['o' - 'a'] / 2, 
            count['n' - 'a']
        )
    }
}
// @lc code=end

