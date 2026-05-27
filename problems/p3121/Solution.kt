/*
 * @lc app=leetcode id=3121 lang=kotlin
 *
 * [3121] Count the Number of Special Characters II
 *
 * https://leetcode.com/problems/count-the-number-of-special-characters-ii/description/
 *
 * algorithms
 * Medium (43.45%)
 * Likes:    210
 * Dislikes: 16
 * Total Accepted:    46.5K
 * Total Submissions: 103.2K
 * Testcase Example:  '"aaAbcBC"'
 *
 * You are given a string word. A letter c is called special if it appears both
 * in lowercase and uppercase in word, and every lowercase occurrence of c
 * appears before the first uppercase occurrence of c.
 * 
 * Return the number of special letters in word.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: word = "aaAbcBC"
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * The special characters are 'a', 'b', and 'c'.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: word = "abc"
 * 
 * Output: 0
 * 
 * Explanation:
 * 
 * There are no special characters in word.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: word = "AbBCab"
 * 
 * Output: 0
 * 
 * Explanation:
 * 
 * There are no special characters in word.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= word.length <= 2 * 10^5
 * word consists of only lowercase and uppercase English letters.
 * 
 * 
 */
package p3121
// @lc code=start
class Solution {
    @Deprecated("Wrong answer")
    fun numberOfSpecialChars0(word: String): Int {
        val hasMeet = mutableSetOf<Char>()
        val special = mutableSetOf<Char>()
        word.forEach {
            if (it.isLowerCase()) {
                hasMeet.add(it.uppercaseChar())
            } else {
                if (it in hasMeet) special.add(it)
            }
        }
        return special.size
    }
    fun numberOfSpecialChars(word: String): Int {
        var lower = 0
        var upper = 0
        var invalid = 0
        for (c in word) {
            val bit = 1 shl (c.lowercaseChar() - 'a')
            if (c >= 'a') {
                if (upper and bit != 0) invalid = invalid or bit
                lower = lower or bit
            } else {
                upper = upper or bit
            }
        }
        return Integer.bitCount(lower and upper and invalid.inv())
    }
}
// @lc code=end
